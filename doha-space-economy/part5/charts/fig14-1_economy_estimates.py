import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

fig, ax = plt.subplots(figsize=(9, 5))
series = [
    ("Space Foundation（实际值）", [2023, 2024, 2025], [570, 613, 686], PALETTE[0], "-", "o"),
    ("Novaspace（2025实际→2034预测）", [2025, 2034], [626, 1010], PALETTE[2], "--", "s"),
    ("麦肯锡/世界经济论坛（2023→2035预测）", [2023, 2035], [630, 1800], ACCENT, "--", "D"),
    ("摩根士丹利（约2020→2040预测）", [2020, 2040], [350, 1000], PALETTE[3], ":", "^"),
]
for name, x, y, c, ls, m in series:
    ax.plot(x, y, ls=ls, marker=m, color=c, lw=2, ms=7, label=name)
    ax.annotate(f"{y[-1]:,}", (x[-1], y[-1]), textcoords="offset points", xytext=(6, -2), fontsize=9, color=c)
    if len(x) == 2 or name.startswith("Space"):
        ax.annotate(f"{y[0]:,}", (x[0], y[0]), textcoords="offset points", xytext=(-8, 8) if x[0] > 2020 else (4, 10), fontsize=9, color=c, ha="right" if x[0] > 2020 else "left")
ax.scatter([2023], [241], color=GREY, marker="x", s=60, zorder=5, label="美国BEA：仅美国，总产出（2023）")
ax.annotate("241", (2023, 241), textcoords="offset points", xytext=(6, -12), fontsize=9, color=GREY)
ax.set_xlim(2019, 2042)
ax.set_ylim(0, 2000)
ax.set_ylabel("十亿美元")
ax.set_title("不同机构对全球太空经济规模的估算与预测（十亿美元）")
ax.legend(loc="upper left", fontsize=9)
source_note(fig, "数据来源：Space Foundation《The Space Report》2025 Q2与2026年7月发布（2023年值按2024年增速7.8%反推）；Novaspace《Space Economy Report》第12版；\n世界经济论坛/麦肯锡《Space: The $1.8 Trillion Opportunity》（2024）；摩根士丹利（2020年研究，2026年仍沿用）；美国经济分析局（BEA）2025年3月。")
save(fig, __file__)
