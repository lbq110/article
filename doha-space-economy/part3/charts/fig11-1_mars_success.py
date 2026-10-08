import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note
import numpy as np

# 按发射次数统计（1960—2020年代已发射的火星任务；在途任务不计）
# 成功 / 部分成功 / 失败
data = {
    "苏联（1960—1988）": (0, 5, 12),
    "俄罗斯（1996—2011）": (0, 0, 2),
    "美国（1964—2020）": (17, 0, 5),
    "欧洲（2003、2016）": (0, 2, 0),
    "日本（1998）": (0, 0, 1),
    "中国（2011、2020）": (1, 0, 1),
    "印度（2013）": (1, 0, 0),
    "阿联酋（2020）": (1, 0, 0),
}
names = list(data)[::-1]
s = np.array([data[k][0] for k in names]); p = np.array([data[k][1] for k in names]); f = np.array([data[k][2] for k in names])
fig, ax = plt.subplots(figsize=(9, 5))
y = np.arange(len(names))
ax.barh(y, s, color=PALETTE[0], height=0.58, label="成功", edgecolor="white", linewidth=1)
ax.barh(y, p, left=s, color=PALETTE[3], height=0.58, label="部分成功", edgecolor="white", linewidth=1)
ax.barh(y, f, left=s + p, color=ACCENT, height=0.58, label="失败", edgecolor="white", linewidth=1)
for yi, a, b, c in zip(y, s, p, f):
    tot = a + b + c
    ax.text(tot + 0.3, yi, f"{tot}次（完全成功{a}、部分成功{b}、失败{c}）", va="center", fontsize=9.5)
ax.set_yticks(y); ax.set_yticklabels(names)
ax.set_xlim(0, 30)
ax.set_xlabel("火星任务数量（次，按航天器计）")
ax.grid(axis="x", color="#E5E5E5"); ax.grid(axis="y", visible=False)
ax.legend(loc="center right", ncol=1)
ax.set_title("各国/地区火星探测任务结果（截至2026年10月，合计48次）")
source_note(fig, "数据来源：NASA NSSDCA、各航天机构公开资料，作者整理。成功＝主要目标达成；部分成功＝如苏联火星2/3/5/6号、福波斯2号、欧洲火星快车（猎兔犬2号着陆器失败）、\nExoMars 2016（斯基亚帕雷利着陆器坠毁）；中国失败1次为2011年随俄福波斯-土壤号发射的萤火一号。2025年发射的ESCAPADE尚在途中，未计入。")
save(fig, __file__)
