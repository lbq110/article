import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note
import numpy as np

yrs = list(range(2015, 2026))
total = [87, 85, 90, 114, 102, 114, 146, 186, 221, 259, 324]
spacex = [7, 8, 18, 21, 13, 25, 31, 61, 96, 134, 165]
china = [19, 22, 18, 39, 34, 39, 55, 64, 67, 68, 92]
russia = [29, 19, 20, 20, 25, 17, 25, 22, 19, 17, 17]
other = [t - a - b - c for t, a, b, c in zip(total, spacex, china, russia)]
fig, ax = plt.subplots(figsize=(9, 4.8))
x = np.array(yrs)
bottom = np.zeros(len(yrs))
for data, lab, col in [(spacex, "SpaceX（猎鹰系列）", PALETTE[0]), (china, "中国", ACCENT),
                       (russia, "俄罗斯", PALETTE[3]), (other, "其他（美国其他公司、欧、日、印、新西兰等）", GREY)]:
    ax.bar(x, data, bottom=bottom, color=col, label=lab, width=0.7, edgecolor="white", linewidth=1)
    bottom += np.array(data)
for xi, t in zip(x, total):
    ax.text(xi, t + 4, str(t), ha="center", fontsize=9.5)
ax.set_xticks(x)
ax.set_ylabel("次")
ax.set_ylim(0, 360)
ax.legend(loc="upper left", fontsize=9.5)
ax.set_title("图2-1　2015—2025年全球轨道发射次数及国别/企业结构（次）")
source_note(fig, "数据来源：Jonathan McDowell发射日志、SpaceNews年度统计（2023—2025年按SpaceNews口径221/259/324次，不含星舰亚轨道试飞）；\nSpaceX年度数据据Space.com；中国2025年92次据国家航天局。2026年上半年全球153次（去年同期145次）。")
save(fig, __file__)
