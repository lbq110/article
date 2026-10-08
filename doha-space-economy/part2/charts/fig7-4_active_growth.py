import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

# (decimal year, count, label, source)
pts = [
    (2019.75, 2218, "2019.9"),
    (2020.25, 2666, "2020.3"),
    (2021.33, 4084, "2021.5"),
    (2023.33, 7560, "2023.5"),
    (2024.54, 10036, "2024.7"),
    (2025.75, 13026, "2025.10"),
    (2026.10, 14543, "2026.2"),
    (2026.75, 16913, "2026.9"),
]
x = [p[0] for p in pts]; yv = [p[1] for p in pts]
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(x, yv, color=PALETTE[0], lw=2, marker="o", ms=7, zorder=3)
for xi, yi, lab in pts:
    if xi > 2025.5 and xi < 2026.5:
        ax.text(xi + 0.12, yi - 300, f"{yi:,}", ha="left", va="top", fontsize=9)
    else:
        ax.text(xi, yi + 650, f"{yi:,}", ha="center", fontsize=9)
ax.set_xlim(2019.3, 2027.2)
ax.set_ylim(0, 19500)
ax.set_xticks(range(2020, 2028))
ax.set_ylabel("在轨活跃卫星（颗）")
ax.annotate("其中星链约10634颗\n（2026年6月）", xy=(2026.45, 15500), xytext=(2023.2, 16200),
            fontsize=9, color="#333333", arrowprops=dict(arrowstyle="->", color=GREY))
ax.set_title("图7-4　全球在轨活跃卫星数量（2019—2026年，时点快照）")
source_note(fig, "数据来源：UCS卫星数据库（2019—2023）；Jonathan McDowell统计（2024年7月、2026年2月/6月/9月）；Look Up × Le Point（2025年10月1日）。\n各来源对“活跃”的界定略有差异，仅示趋势。")
save(fig, __file__)
