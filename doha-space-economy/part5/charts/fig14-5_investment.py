import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note
import numpy as np

fig, ax = plt.subplots(figsize=(8.5, 4.6))
labels = ["2023", "2024", "2025", "2026上半年"]
seraphim = [6.9, 8.6, 12.4, 15.5]
spacecap = [17.9, 33.5, 55.3, 67.6]
x = np.arange(4)
w = 0.38
b1 = ax.bar(x - w/2, seraphim, w, color=PALETTE[0], label="Seraphim：太空科技风险投资（窄口径）")
b2 = ax.bar(x + w/2, spacecap, w, color=PALETTE[3], label="Space Capital：全太空经济股权投资（宽口径）")
for b, v in zip(list(b1) + list(b2), seraphim + spacecap):
    ax.text(b.get_x() + b.get_width()/2, v + 1, f"{v:g}", ha="center", fontsize=9.5)
ax.set_xticks(x, labels)
ax.set_ylim(0, 78)
ax.set_ylabel("十亿美元")
ax.set_title("全球太空领域私人投资（十亿美元）")
ax.legend(loc="upper left", fontsize=9)
source_note(fig, "数据来源：Seraphim Space Index（2024年Q4、2025年全年、2026年Q1/Q2报告；2026上半年=80+75亿美元）；Space Capital《Space Investment Quarterly》\n（2023年179亿；2025年553亿；2024年按2025年同比增长65%反推；2026上半年=Q1 360亿+Q2 316亿）。两家口径不同，不可直接相加或比较。")
save(fig, __file__)
