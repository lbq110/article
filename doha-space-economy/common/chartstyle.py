"""Shared chart style for all parts. Usage in a chart script:

    import sys, pathlib
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
    from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

    fig, ax = plt.subplots(figsize=(8, 4.5))
    ...
    source_note(fig, "数据来源：UCS、Jonathan McDowell")
    save(fig, __file__)          # writes charts/<script-name>.png next to the script
"""
import logging
import pathlib
import matplotlib
import numpy as np

logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from matplotlib import font_manager
from matplotlib import patheffects as pe
from matplotlib.collections import Collection
from matplotlib.lines import Line2D
from matplotlib.patches import FancyBboxPatch, Patch, Rectangle
from matplotlib.text import Text

_FONT = "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"
font_manager.fontManager.addfont(_FONT)
_NAME = font_manager.FontProperties(fname=_FONT).get_name()

# "Deep space" theme: navy night-sky surface, faint stars, glowing marks.
# Categorical order validated with dataviz validate_palette.js (--mode dark,
# surface #0B1220): lightness band, chroma, CVD >= 8 adjacent, contrast >= 3:1.
SURFACE = "#0B1220"
SURFACE_2 = "#131C2E"          # panels / label boxes
TEXT = "#E8EEF7"
TEXT_2 = "#9AA8BD"
GRIDC = "#1F2A3F"
PALETTE = ["#1793D1", "#E8622A", "#139E6E", "#B58600", "#8B6CF0", "#E0559A", "#4C7FE6", "#E24A4A"]
ACCENT = "#E8622A"
GREY = "#5B6B85"
GLOW = "#38BDF8"

plt.rcParams.update({
    "font.family": _NAME,
    "font.sans-serif": [_NAME],
    "axes.unicode_minus": False,
    "font.size": 11,
    "text.color": TEXT,
    "axes.labelcolor": TEXT_2,
    "xtick.color": TEXT_2,
    "ytick.color": TEXT_2,
    "axes.titlesize": 15,
    "axes.titleweight": "bold",
    "axes.titlecolor": TEXT,
    "axes.titlelocation": "left",
    "axes.titlepad": 14,
    "axes.labelsize": 11,
    "axes.facecolor": (0, 0, 0, 0),
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.spines.left": False,
    "axes.edgecolor": "#3A4A66",
    "axes.grid": True,
    "axes.grid.axis": "y",
    "grid.color": GRIDC,
    "grid.linewidth": 0.8,
    "axes.axisbelow": True,
    "axes.prop_cycle": matplotlib.cycler(color=PALETTE),
    "xtick.major.size": 0,
    "ytick.major.size": 0,
    "lines.linewidth": 2.4,
    "lines.markersize": 6,
    "patch.edgecolor": SURFACE,
    "legend.frameon": False,
    "legend.labelcolor": TEXT,
    "figure.dpi": 100,
    "savefig.dpi": 200,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.35,
    "figure.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
})


def source_note(fig, text):
    """Small muted source line at bottom-left of the figure."""
    fig.text(0.01, -0.02, text, ha="left", va="top", fontsize=8.5, color=TEXT_2)


# ---------------------------------------------------------------- dark fix-up
# Scripts written for a white page may hard-code dark ink or white boxes; remap
# them at save time so every chart reads on the night-sky surface.

def _lum(c):
    r, g, b, _ = mcolors.to_rgba(c)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def _sat(c):
    r, g, b, _ = mcolors.to_rgba(c)
    return max(r, g, b) - min(r, g, b)


def _ink(c, light=TEXT):
    """Dark neutral ink -> light ink; keeps saturated colours and alpha."""
    try:
        rgba = mcolors.to_rgba(c)
    except (ValueError, TypeError):
        return c
    if rgba[3] == 0:
        return c
    if _sat(c) < 0.18 and _lum(c) < 0.45:
        return mcolors.to_rgba(light, rgba[3])
    return c


def _paper(c):
    """White / near-white fills -> panel colour."""
    try:
        rgba = mcolors.to_rgba(c)
    except (ValueError, TypeError):
        return c
    if rgba[3] > 0 and _sat(c) < 0.12 and _lum(c) > 0.85:
        return mcolors.to_rgba(SURFACE_2, rgba[3])
    return c


def _fix_text(t):
    t.set_color(_ink(t.get_color()))
    box = t.get_bbox_patch()
    if box is not None:
        box.set_facecolor(_paper(box.get_facecolor()))
        ec = box.get_edgecolor()
        box.set_edgecolor(_ink(ec, GREY) if _lum(ec) < 0.45 else _paper(ec))
    arrow = getattr(t, "arrow_patch", None)
    if arrow is not None:
        arrow.set_color(_ink(arrow.get_edgecolor(), TEXT_2))


def _fix_axes(ax):
    for t in ax.texts:
        _fix_text(t)
    for t in (ax.title, ax._left_title, ax._right_title, ax.xaxis.label, ax.yaxis.label):
        _fix_text(t)
    for ln in ax.lines:
        c = ln.get_color()
        if _sat(c) < 0.12 and _lum(c) > 0.7:     # pale guide/stem lines meant for white paper
            ln.set_color(mcolors.to_rgba("#3A4A66", mcolors.to_rgba(c)[3]))
        else:
            ln.set_color(_ink(c, TEXT_2))
        ln.set_markerfacecolor(_paper(_ink(ln.get_markerfacecolor(), TEXT_2)))
        ln.set_markeredgecolor(_paper(_ink(ln.get_markeredgecolor(), TEXT_2)))
        x = ln.get_xdata()
        # glow on real data lines (not reference lines / markers-only)
        if ln.get_linestyle() in ("-", "solid") and ln.get_linewidth() >= 1.5 and np.size(x) > 2:
            ln.set_path_effects([pe.Stroke(linewidth=ln.get_linewidth() + 5, foreground=ln.get_color(), alpha=0.18),
                                 pe.Normal()])
    for p in ax.patches:
        p.set_facecolor(_paper(p.get_facecolor()))
        ec = p.get_edgecolor()
        if mcolors.to_rgba(ec)[3] > 0 and _sat(ec) < 0.12 and _lum(ec) > 0.85:
            p.set_edgecolor(SURFACE)            # white separators -> surface gaps
        elif mcolors.to_rgba(ec)[3] > 0:
            p.set_edgecolor(_ink(ec, GREY))
    for c in ax.collections:
        try:
            c.set_edgecolor([_ink(e, TEXT_2) for e in c.get_edgecolor()])
        except Exception:
            pass
    leg = ax.get_legend()
    if leg is not None:
        for t in leg.get_texts():
            t.set_color(_ink(t.get_color()))
        if leg.get_title():
            _fix_text(leg.get_title())
        fr = leg.get_frame()
        fr.set_facecolor(SURFACE_2)
        fr.set_edgecolor(GRIDC)
    for sp in ax.spines.values():
        sp.set_edgecolor(_ink(sp.get_edgecolor(), "#3A4A66"))
    for gl in ax.get_xgridlines() + ax.get_ygridlines():
        gl.set_color(GRIDC)
    ax.tick_params(colors=TEXT_2)
    for lab in ax.get_xticklabels() + ax.get_yticklabels():
        lab.set_color(_ink(lab.get_color(), TEXT_2))
    if ax.get_facecolor()[3] > 0 and _lum(ax.get_facecolor()) > 0.85:
        ax.set_facecolor((0, 0, 0, 0))


def _starfield(fig, rect, n=220, seed=7):
    """Night-sky backdrop filling `rect` (figure-fraction [x, y, w, h])."""
    rng = np.random.default_rng(seed)
    bg = fig.add_axes(rect, zorder=-10)
    bg.set_axis_off()
    yy, xx = np.mgrid[0:1:300j, 0:1:400j]
    # soft nebula glow centred near the figure's upper-right corner
    glow = np.exp(-(((xx - 0.68) / 0.22) ** 2 + ((yy - 0.70) / 0.26) ** 2))
    cmap = mcolors.LinearSegmentedColormap.from_list("sky", [SURFACE, "#172A52"])
    bg.imshow(glow, extent=[0, 1, 0, 1], origin="lower", cmap=cmap, aspect="auto", zorder=0)
    x, y = rng.random(n), rng.random(n)
    size = rng.choice([0.5, 0.9, 1.6, 2.8], size=n, p=[0.55, 0.28, 0.13, 0.04])
    bg.scatter(x, y, s=size, c="white", alpha=0.32, linewidths=0, zorder=1)
    bg.set_xlim(0, 1)
    bg.set_ylim(0, 1)


def _accent(fig):
    """Short glowing bar just above the first titled axes' title (signature mark)."""
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    sup = getattr(fig, "_suptitle", None)
    cands = [sup] if sup is not None and sup.get_text() else []
    for ax in fig.axes:
        cands += [t for t in (ax._left_title, ax.title) if t.get_text()]
    for t in cands[:1]:
        bb = t.get_window_extent(r).transformed(fig.transFigure.inverted())
        h = 0.012
        fig.add_artist(Rectangle((bb.x0, bb.y1 + 0.018), 0.06, h, transform=fig.transFigure,
                                 color=GLOW, zorder=5, clip_on=False))
        return


def save(fig, script_file):
    fig.patch.set_facecolor(SURFACE)
    for ax in fig.axes:
        _fix_axes(ax)
    for t in fig.texts:
        _fix_text(t)
    for leg in fig.legends:
        for t in leg.get_texts():
            t.set_color(_ink(t.get_color()))
    if getattr(fig, "_suptitle", None) is not None:
        _fix_text(fig._suptitle)
    _accent(fig)
    # measure the content first, then lay the sky exactly under it
    fig.canvas.draw()
    pad = plt.rcParams["savefig.pad_inches"]
    bb = fig.get_tightbbox(fig.canvas.get_renderer()).padded(pad)   # inches
    W, H = fig.get_size_inches()
    _starfield(fig, [bb.x0 / W, bb.y0 / H, bb.width / W, bb.height / H])
    out = pathlib.Path(script_file).with_suffix(".png")
    fig.savefig(out, facecolor=SURFACE, bbox_inches=bb, pad_inches=0)
    plt.close(fig)
    print("saved", out)
    return out
