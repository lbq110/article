import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

fig, ax = plt.subplots(figsize=(8.5, 4.6))
labels = ["2022年末", "2023年末", "2024年末", "2025年末", "2026年3月末", "2026年6月末"]
vals = [1.0, 2.3, 4.4, 8.9, 10.3, 12.0]
colors = [GREY] + [PALETTE[0]] * 3 + [ACCENT] * 2
bars = ax.bar(labels, vals, color=colors, width=0.6)
for b, v in zip(bars, vals):
    ax.text(b.get_x() + b.get_width() / 2, v + 0.25, f"{v:g}", ha="center", fontsize=10.5, fontweight="bold")
ax2 = ax.twinx()
arpu_x = [1, 5]
ax2.plot(arpu_x, [99, 66], color=PALETTE[3], marker="o", lw=2, ls="--")
ax2.annotate("月均ARPU约99美元", (1, 99), textcoords="offset points", xytext=(8, 6), fontsize=9, color=PALETTE[3])
ax2.annotate("约66美元", (5, 66), textcoords="offset points", xytext=(-48, -4), ha="right", fontsize=9, color=PALETTE[3], bbox=dict(boxstyle="round,pad=0.25", fc="#0B1220", ec="none", alpha=0.85))
ax2.set_ylim(0, 140)
ax2.set_ylabel("每用户月均收入（美元）", color=PALETTE[3])
ax2.spines["right"].set_visible(True)
ax2.grid(False)
ax.set_ylim(0, 14)
ax.set_ylabel("活跃用户（百万）")
ax.set_title("星链活跃用户数增长（百万）与单用户收入下降")
source_note(fig, "数据来源：SpaceX招股说明书（S-1，2026年5月）及2026年第二季度财报（2026年8月4日）；2022年末约100万为SpaceX当时公开宣布的里程碑（灰色）。\nARPU为二手报道转引S-1数据。")
save(fig, __file__)
