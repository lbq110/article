import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

fig, ax = plt.subplots(figsize=(9, 4.8))
orb = [(2001, 20, "蒂托·联盟号\n约2000万"), (2009, 35, "联盟号游客\n约3500万"), (2022, 55, "Ax-1\n约5500万"), (2025, 70, "Ax-4（报道）\n约7000万")]
sub = [(2005, 0.2, "维珍银河早期预订\n20万"), (2013, 0.25, "25万"), (2021, 0.45, "45万"), (2023, 0.6, "60万"), (2026, 0.75, "75万")]
ax.plot([p[0] for p in orb], [p[1] for p in orb], marker="o", color=PALETTE[0], lw=2, label="轨道级（国际空间站访问）")
ax.plot([p[0] for p in sub], [p[1] for p in sub], marker="s", color=ACCENT, lw=2, label="亚轨道（维珍银河票价）")
for x, y, t in orb:
    ax.annotate(t, (x, y), textcoords="offset points", xytext=(0, 10), ha="center", fontsize=8.5, color=PALETTE[0])
for x, y, t in sub:
    ax.annotate(t, (x, y), textcoords="offset points", xytext=(0, -26), ha="center", fontsize=8.5, color=ACCENT)
ax.set_yscale("log")
from matplotlib.ticker import FixedLocator, FuncFormatter, NullLocator
ax.yaxis.set_major_locator(FixedLocator([0.1, 0.3, 1, 3, 10, 30, 100]))
ax.yaxis.set_minor_locator(NullLocator())
ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:g}"))
ax.set_ylim(0.08, 300)
ax.set_xlim(1999, 2028)
ax.set_ylabel("单人价格（百万美元，对数坐标）")
ax.set_title("太空旅游票价：不降反升（百万美元，名义价格）")
ax.legend(loc="upper left", fontsize=9)
source_note(fig, "数据来源：公开报道整理——Space Adventures/蒂托（2001）；Axiom联合创始人对Ax-1票价的说明；Business Insider关于Ax-4座位约7000万美元的报道；\n维珍银河历次公告及彭博、The Register报道（2026年恢复售票75万美元）。均为名义价格，未经通胀调整；早期维珍预订价与联盟号游客价为常见报道数，请作者复核。")
save(fig, __file__)
