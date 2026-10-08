import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note
import numpy as np

fig, ax = plt.subplots(figsize=(8.5, 4.6))
seg = ["连接（星链）", "航天（发射等）", "人工智能（xAI）"]
rev = [11.4, 4.1, 3.2]
op = [4.4, -0.657, -6.4]
x = np.arange(3)
w = 0.36
b1 = ax.bar(x - w/2, rev, w, color=PALETTE[0], label="2025年收入")
b2 = ax.bar(x + w/2, op, w, color=[ACCENT if v < 0 else PALETTE[2] for v in op], label="2025年经营利润")
for b, v in zip(b1, rev):
    ax.text(b.get_x() + b.get_width()/2, v + 0.3, f"{v:g}", ha="center", fontsize=10)
for b, v in zip(b2, op):
    ax.text(b.get_x() + b.get_width()/2, v + (0.3 if v >= 0 else -0.9), f"{v:g}", ha="center", fontsize=10)
ax.axhline(0, color="#444444", lw=0.8)
ax.set_xticks(x, seg)
ax.set_ylim(-8, 14)
ax.set_ylabel("十亿美元")
ax.set_title("SpaceX 2025年分部收入与经营利润（十亿美元）")
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=PALETTE[0], label="收入"), Patch(color=PALETTE[2], label="经营利润"), Patch(color=ACCENT, label="经营亏损")], loc="upper right", fontsize=9, ncol=3)
ax.text(0.5, -4.0, "全公司合计：收入187亿美元\n调整后EBITDA约66亿美元\n净亏损约49亿美元", fontsize=9.5, ha="center", va="center", color="#333333", bbox=dict(boxstyle="round", fc="#F5F5F5", ec="#CCCCCC"))
source_note(fig, "数据来源：SpaceX招股说明书（S-1）经Motley Fool、Tomasz Tunguz等二手分析转引；xAI于2026年2月并入SpaceX，2025年分部数据为合并口径。")
save(fig, __file__)
