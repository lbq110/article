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

logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

_FONT = "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"
font_manager.fontManager.addfont(_FONT)
_NAME = font_manager.FontProperties(fname=_FONT).get_name()

# Calm, print-friendly categorical palette (works in B/W print too)
PALETTE = ["#1F4E79", "#C0504D", "#4F9A94", "#E39B3B", "#7D5BA6", "#8C8C8C", "#2E86C1", "#A0522D"]
ACCENT = "#C0504D"
GREY = "#8C8C8C"

plt.rcParams.update({
    "font.family": _NAME,
    "font.sans-serif": [_NAME],
    "axes.unicode_minus": False,
    "font.size": 11,
    "axes.titlesize": 14,
    "axes.titleweight": "bold",
    "axes.titlepad": 12,
    "axes.labelsize": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.edgecolor": "#444444",
    "axes.grid": True,
    "axes.grid.axis": "y",
    "grid.color": "#E5E5E5",
    "grid.linewidth": 0.8,
    "axes.axisbelow": True,
    "axes.prop_cycle": matplotlib.cycler(color=PALETTE),
    "legend.frameon": False,
    "figure.dpi": 100,
    "savefig.dpi": 200,
    "savefig.bbox": "tight",
    "figure.facecolor": "white",
})


def source_note(fig, text):
    """Small grey source line at bottom-left of the figure."""
    fig.text(0.01, -0.02, text, ha="left", va="top", fontsize=8.5, color="#666666")


def save(fig, script_file):
    out = pathlib.Path(script_file).with_suffix(".png")
    fig.savefig(out)
    plt.close(fig)
    print("saved", out)
    return out
