import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

rows = [
    ("NSR《月球市场分析》第1版（2021）\n约140次任务，2020—2030年累计", 42.3, PALETTE[5]),
    ("NSR《月球市场分析》第2版（2022）\n250余次任务，未来十年累计", 105, PALETTE[5]),
    ("Analysys Mason《月球市场》第4版\n450余次任务，2023—2033年累计", 151, PALETTE[0]),
    ("普华永道（2021）\n至2040年，1420亿欧元≈1700亿美元", 170, PALETTE[3]),
    ("普华永道（2026，第2版）\n2026—2050年累计收入（区间上限）", 127.3, PALETTE[3]),
]
fig, ax = plt.subplots(figsize=(9, 4.8))
y = list(range(len(rows)))[::-1]
ax.barh(y, [r[1] for r in rows], color=[r[2] for r in rows], height=0.55)
for yi, r in zip(y, rows):
    ax.text(r[1] + 3, yi, f"{r[1]:g}", va="center", fontsize=10)
# 普华永道2026区间下限
ax.plot([93.9, 93.9], [y[-1] - 0.3, y[-1] + 0.3], color="white", lw=2)
ax.text(91.5, y[-1], "区间下限93.9", ha="right", va="center", fontsize=8.5, color="white")
ax.set_yticks(y); ax.set_yticklabels([r[0] for r in rows], fontsize=9)
ax.set_xlim(0, 200)
ax.set_xlabel("十亿美元")
ax.grid(axis="x", color="#E5E5E5"); ax.grid(axis="y", visible=False)
ax.set_title("各机构对月球经济规模的预测（累计值）")
source_note(fig, "数据来源：NSR（2021、2022）、Analysys Mason（2023）、PwC《Lunar Market Assessment》（2021；2026年第2版）。\n各机构统计口径、时间窗口不同，政府任务支出占主体，不宜直接横向比较；PwC 2021报告原文为1420亿欧元，按当时汇率约合1700亿美元。")
save(fig, __file__)
