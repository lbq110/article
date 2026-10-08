import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

total = 4517
items = [("SpaceX 星链", 3180), ("中国（全部）", 377), ("亚马逊 柯伊伯", 180),
         ("美国国家侦察局（星盾平台）", 99), ("其他所有运营者", total - 3180 - 377 - 180 - 99)]
labels = [i[0] for i in items][::-1]
vals = [i[1] for i in items][::-1]
colors = [GREY, PALETTE[3], PALETTE[2], ACCENT, PALETTE[0]][::-1]
colors = [PALETTE[0], ACCENT, PALETTE[2], PALETTE[3], GREY][::-1]
fig, ax = plt.subplots(figsize=(8.5, 4.2))
bars = ax.barh(labels, vals, color=colors, height=0.6)
for b, v in zip(bars, vals):
    ax.text(v + 40, b.get_y() + b.get_height() / 2, f"约{v:,}颗（{v/total:.0%}）", va="center", fontsize=10)
ax.set_xlim(0, 4200)
ax.grid(axis="x", color="#E5E5E5"); ax.grid(axis="y", visible=False)
ax.set_xlabel("颗")
ax.set_title("图1-2　2025年全球入轨卫星的主要来源（约4,500颗）")
source_note(fig, "数据来源：总数4,517颗、星链约3,180颗据Jonathan McDowell统计（经Payload、Ars Technica等转引）；中国约377颗据国内媒体年度统计；\n柯伊伯、NRO数据据ISRO《ISSAR 2025》。各项口径与统计时点略有差异，仅示意结构，合计不严格等于总数。")
save(fig, __file__)
