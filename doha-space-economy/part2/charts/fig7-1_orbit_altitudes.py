import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(9, 5.2))
ax.set_xscale("log")
ax.set_xlim(70, 3e6)
ax.set_ylim(0, 10)
ax.grid(False)
ax.spines["left"].set_visible(False)
ax.set_yticks([])

# bands (km)
bands = [
    (100, 2000, "低地球轨道 LEO\n（≤2000 km）", PALETTE[0], 8.2),
    (2000, 35786, "中地球轨道 MEO\n（2000–35786 km）", PALETTE[2], 8.2),
    (35786, 400000, "地球同步轨道之外\n（高轨/地月空间）", PALETTE[4], 8.2),
]
for lo, hi, label, c, y in bands:
    ax.axvspan(lo, hi, ymin=0.70, ymax=0.98, color=c, alpha=0.18, lw=0)
    ax.text((lo*hi)**0.5, y, label, ha="center", va="center", fontsize=9.5, color="#222222")

# Van Allen belts
ax.axvspan(1000, 12000, ymin=0.52, ymax=0.62, color=ACCENT, alpha=0.25, lw=0)
ax.text((1000*12000)**0.5, 5.7, "内辐射带（质子为主）\n约1000–12000 km", ha="center", va="center", fontsize=8)
ax.axvspan(13000, 60000, ymin=0.52, ymax=0.62, color=PALETTE[3], alpha=0.30, lw=0)
ax.text(65000, 5.7, "← 外辐射带（电子为主）\n   约13000–60000 km", ha="left", va="center", fontsize=8)

# markers
marks = [
    (100, "卡门线 100", 4.3),
    (275, "星链V3入轨 ~275", 3.5),
    (400, "中国空间站/ISS ~400", 2.7),
    (480, "星链主壳层 480–550", 1.9),
    (800, "太阳同步轨道 600–800", 1.1),
    (21500, "北斗/GPS 中轨 ~2万", 4.3),
    (35786, "地球静止轨道 35786", 3.4),
    (384400, "月球 38.4万", 2.5),
    (1.5e6, "日地L1/L2 约150万", 1.6),
]
for x, label, y in marks:
    ax.axvline(x, ymin=0, ymax=y/10 + 0.03, color="#444444", lw=1)
    ax.plot([x], [y + 0.3], marker="o", ms=5, color="#1F1F1F")
    ax.text(x * 1.08, y + 0.3, label, fontsize=8.8, va="center", ha="left")

ax.set_xlabel("距地面高度（千米，对数刻度）")
ax.set_title("图7-1　地球轨道高度带、辐射带与典型航天器位置")
source_note(fig, "数据来源：NASA、ESA轨道分类惯例；范艾伦辐射带范围据NICT等资料，为大致区间，随空间天气变化。作者整理。")
save(fig, __file__)
