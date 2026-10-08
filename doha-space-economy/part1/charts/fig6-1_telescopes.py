import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

# name, launch, aperture (m), band, note, launched?
t = [("哈勃（1990）", 2.4, "紫外—可见光—近红外", "近地轨道（初始约600公里）", True),
     ("钱德拉（1999）", 1.2, "X射线", "大椭圆轨道", True),
     ("斯皮策（2003—2020）", 0.85, "红外", "尾随地球日心轨道", True),
     ("开普勒（2009—2018）", 0.95, "可见光（凌星测光；主镜1.4米）", "尾随地球日心轨道", True),
     ("盖亚（2013—2025）", 1.45, "可见光（两面1.45×0.5米矩形主镜）", "日地L2", True),
     ("韦伯（2021）", 6.5, "近—中红外", "日地L2", True),
     ("欧几里得（2023）", 1.2, "可见光+近红外", "日地L2", True),
     ("罗曼（2026.8）", 2.4, "近红外广域巡天", "日地L2", True),
     ("巡天CSST（约2027）", 2.0, "紫外—可见光—近红外", "与天宫共轨", False)]
t = t[::-1]
fig, ax = plt.subplots(figsize=(9.5, 5.2))
for i, (name, ap, band, orbit, done) in enumerate(t):
    if done:
        ax.barh(i, ap, color=ACCENT if "韦伯" in name else PALETTE[0], height=0.62)
    else:
        ax.barh(i, ap, color="white", edgecolor=PALETTE[0], hatch="////", height=0.62, linewidth=0.9)
    ax.text(ap + 0.08, i, f"{ap}米 · {band} · {orbit}", va="center", fontsize=9.3)
ax.set_yticks(range(len(t)))
ax.set_yticklabels([x[0] for x in t])
ax.set_xlim(0, 11.5)
ax.set_xlabel("主镜口径（米）")
ax.grid(axis="x", color="#E5E5E5"); ax.grid(axis="y", visible=False)
ax.set_title("图6-1　主要空间望远镜的口径、波段与轨道位置")
source_note(fig, "数据来源：NASA、ESA、中国载人航天工程办公室公开资料。斜线柱为计划中项目（发射时间以官方最新公布为准）。\n欧空局PLATO（计划2027年初发射）由26台口径12厘米相机组成，未列入。")
save(fig, __file__)
