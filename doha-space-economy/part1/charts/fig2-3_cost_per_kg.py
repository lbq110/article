import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

items = [("航天飞机（1981—2011）", 54500, "a"), ("土星5号（1967—1973）", 5400, "a"),
         ("猎鹰9号（2010— ，标价）", 2600, "a"), ("猎鹰重型（2018— ，标价）", 1500, "a"),
         ("猎鹰9号复用·SpaceX内部成本（估算）", 1000, "e"), ("星舰完全复用（SpaceX目标）", 200, "t")]
labels = [i[0] for i in items][::-1]
vals = [i[1] for i in items][::-1]
kinds = [i[2] for i in items][::-1]
fig, ax = plt.subplots(figsize=(9, 4.6))
for lab, v, k in zip(labels, vals, kinds):
    if k == "a":
        ax.barh(lab, v, color=PALETTE[0], height=0.6)
    else:
        ax.barh(lab, v, color="white", edgecolor=ACCENT if k == "t" else PALETTE[0], hatch="////", height=0.6, linewidth=0.9)
    txt = f"约{v:,}" if k != "t" else "≤200（目标；长期目标更低）"
    ax.text(v * 1.12, lab, txt, va="center", fontsize=10)
ax.set_xscale("log")
ax.set_xlim(80, 300000)
ax.grid(axis="x", color="#E5E5E5"); ax.grid(axis="y", visible=False)
ax.set_xlabel("美元/公斤（对数坐标，近地轨道，2021年美元）")
ax.set_title("图2-3　进入近地轨道的单位成本：半个世纪下降两个数量级")
source_note(fig, "数据来源：实心柱据CSIS Aerospace Security Project与NASA Harry Jones (2018) 的整理（按2021年美元、以最大近地轨道运力折算）；\n斜线柱为业界估算或SpaceX公开目标，并非实际成交价。航天飞机按项目全寿命总成本÷135次计算。")
save(fig, __file__)
