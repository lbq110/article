import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

items = [("航天飞机（1981—2011）", 54500, "a"), ("土星5号（1967—1973）", 5000, "a"),
         ("猎鹰9号（2026年标价7400万美元）", 3200, "a"), ("猎鹰9号（2018年标价6200万美元）", 2720, "a"),
         ("猎鹰重型（2018年标价）", 1400, "a"),
         ("猎鹰9号复用·边际成本（估算）", 1000, "e"), ("星舰完全复用（业界估算）", 200, "t")]
labels = [i[0] for i in items][::-1]
vals = [i[1] for i in items][::-1]
kinds = [i[2] for i in items][::-1]
fig, ax = plt.subplots(figsize=(9, 5.0))
for lab, v, k in zip(labels, vals, kinds):
    if k == "a":
        ax.barh(lab, v, color=PALETTE[0], height=0.6)
    else:
        ax.barh(lab, v, color="white", edgecolor=ACCENT if k == "t" else PALETTE[0], hatch="////", height=0.6, linewidth=0.9)
    txt = f"约{v:,}" if k != "t" else "约200（估算；马斯克设想更低）"
    ax.text(v * 1.12, lab, txt, va="center", fontsize=10)
ax.set_xscale("log")
ax.set_xlim(80, 300000)
ax.grid(axis="x", color="#E5E5E5"); ax.grid(axis="y", visible=False)
ax.set_xlabel("美元/公斤（对数坐标，近地轨道，按最大运力满载折算，当年美元）")
ax.set_title("图2-3　进入近地轨道的单位成本：从航天飞机到猎鹰重型降至约四十分之一")
source_note(fig, "数据来源：航天飞机、土星5号、猎鹰9号/重型（2018年）据NASA Harry Jones (2018)；猎鹰9号2026年标价据SpaceX。\n斜线柱为估算：边际成本据马斯克2020年所述约1,500万美元/次；星舰为业界常引用估算，非实际价格。航天飞机按约15亿美元/次÷27.5吨。")
save(fig, __file__)
