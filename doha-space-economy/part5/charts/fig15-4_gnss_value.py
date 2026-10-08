import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.8), gridspec_kw={"width_ratios": [1.3, 1], "wspace": 0.55})
yrs = ["2019", "2020", "2021", "2022", "2023", "2024", "2025"]
vals = [3450, 4033, 4690, 5007, 5362, 5758, 6290]
b = ax1.bar(yrs, vals, color=[PALETTE[0]] * 6 + [ACCENT], width=0.6)
for bb, v in zip(b, vals):
    ax1.text(bb.get_x() + bb.get_width()/2, v + 80, f"{v:,}", ha="center", fontsize=9)
ax1.set_ylim(0, 8000)
ax1.set_title("中国卫星导航与位置服务产业总产值（亿元）", fontsize=12)
ax1.text(-0.4, 7800, "2025年按新口径“北斗时空产业”\n总产值达13,323亿元", fontsize=9, color=ACCENT, va="top")
sect = ["电信（授时等）", "车载信息服务", "手机位置服务", "其余七个行业"]
sv = [685.9, 325, 215, 174]
b2 = ax2.barh(sect[::-1], sv[::-1], color=[GREY, PALETTE[2], PALETTE[2], PALETTE[2]], height=0.6)
for bb, v in zip(b2, sv[::-1]):
    ax2.text(v + 10, bb.get_y() + bb.get_height()/2, f"{v:g}", va="center", fontsize=9.5)
ax2.set_xlim(0, 820)
ax2.grid(axis="x", color="#E5E5E5"); ax2.grid(axis="y", visible=False)
ax2.set_title("GPS对美国私营部门的累计经济收益\n（1984–2017年，十亿美元，合计约1.4万亿）", fontsize=11)
source_note(fig, "数据来源：中国卫星导航定位协会历年《中国卫星导航与位置服务产业发展白皮书》及《2026中国北斗时空产业发展白皮书》（2026年5月18日）；\nRTI International受NIST委托《Economic Benefits of the Global Positioning System》（2019）。“其余七个行业”为总额减三大项的推算值。")
save(fig, __file__)
