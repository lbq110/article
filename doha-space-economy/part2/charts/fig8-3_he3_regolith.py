import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

conc = [4, 10, 20]   # ppb by mass
labels = ["月壤平均\n约4 ppb", "样品高值\n约10 ppb", "富钛月海估计\n约20 ppb"]
tonnes = [1e9/c/1000 for c in conc]   # tonnes regolith per kg He-3
value = [20e6 / t for t in tonnes]     # USD per tonne regolith at $20M/kg
fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.4))
ax = axes[0]
ax.bar(range(3), [t/1e4 for t in tonnes], color=PALETTE[0], width=0.55)
for i, t in enumerate(tonnes):
    ax.text(i, t/1e4 + 0.5, f"{t/1e4:.0f}万吨", ha="center", fontsize=10)
ax.set_xticks(range(3)); ax.set_xticklabels(labels, fontsize=9.5)
ax.set_ylabel("万吨月壤")
ax.set_ylim(0, 29)
ax.set_title("提取1公斤氦-3需处理的月壤", fontsize=12)
ax = axes[1]
ax.bar(range(3), value, color=PALETTE[3], width=0.55)
for i, v in enumerate(value):
    ax.text(i, v + 10, f"{v:.0f}美元", ha="center", fontsize=10)
ax.set_xticks(range(3)); ax.set_xticklabels(labels, fontsize=9.5)
ax.set_ylabel("美元/吨月壤")
ax.set_ylim(0, 460)
ax.set_title("每吨月壤所含氦-3的理论价值", fontsize=12)
fig.suptitle("图8-3　月球氦-3的“品位账”：按100%回收率计算", fontsize=14, fontweight="bold", y=1.02)
source_note(fig, "数据来源：氦-3丰度据月球资源综述（arXiv:1410.6865）、Apollo 11样品测量等；价格按Interlune所称约2000万美元/公斤。作者测算，未计回收损失与开采成本。")
save(fig, __file__)
