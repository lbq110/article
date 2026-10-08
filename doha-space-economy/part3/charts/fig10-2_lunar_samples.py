import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

names = ["苏联月球16/20/24号\n（1970—1976，3次无人）", "中国嫦娥五号\n（2020，月球正面）", "中国嫦娥六号\n（2024，月球背面）", "美国阿波罗11—17号\n（1969—1972，6次载人）"]
grams = [326, 1731, 1935.3, 382000]
labels = ["约0.3公斤", "1731克", "1935.3克", "约382公斤"]
colors = [GREY, PALETTE[0], PALETTE[0], PALETTE[3]]
fig, ax = plt.subplots(figsize=(8.5, 4.4))
y = range(len(names))[::-1]
ax.barh(list(y), grams, color=colors, height=0.55)
ax.set_xscale("log")
ax.set_yticks(list(y))
ax.set_yticklabels(names, fontsize=9.5)
for yi, g, l in zip(y, grams, labels):
    ax.text(g * 1.25, yi, l, va="center", fontsize=10)
ax.set_xlim(50, 3e6)
ax.set_xlabel("返回地球的月球样品质量（克，对数坐标）")
ax.grid(axis="x", color="#E5E5E5"); ax.grid(axis="y", visible=False)
ax.set_title("人类从月球带回的样品质量对比")
source_note(fig, "数据来源：NASA（阿波罗约382公斤）、CNSA（嫦娥五号1731克、嫦娥六号1935.3克）；苏联三次采样分别约101克、55克（一说30克）、170克，合计约301—326克。")
save(fig, __file__)
