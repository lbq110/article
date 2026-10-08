import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

# name, sea-level thrust (tf), chamber pressure (bar), propellant/cycle
eng = [("梅林1D（SpaceX）", 86, 97, "煤油·燃气发生器"), ("天鹊TQ-12（蓝箭）", 67, 100, "甲烷·燃气发生器"),
       ("YF-100（中国）", 120, 180, "煤油·富氧补燃"), ("RS-25（美国）", 190, 206, "液氢·富燃补燃"),
       ("BE-4（蓝色起源）", 245, 134, "甲烷·富氧补燃"), ("RD-180（俄罗斯）", 390, 267, "煤油·富氧补燃"),
       ("猛禽2（SpaceX）", 230, 300, "甲烷·全流量补燃"), ("猛禽3（SpaceX）", 280, 350, "甲烷·全流量补燃")]
names = [f"{e[0]}\n{e[3]}" for e in eng]
fig, axes = plt.subplots(1, 2, figsize=(10, 5.2), sharey=True)
for ax, idx, title, unit in [(axes[0], 1, "海平面推力", "吨力"), (axes[1], 2, "燃烧室压力", "bar")]:
    vals = [e[idx] for e in eng]
    cols = [ACCENT if "猛禽" in e[0] else PALETTE[0] for e in eng]
    bars = ax.barh(names, vals, color=cols, height=0.6)
    for b, v in zip(bars, vals):
        ax.text(v + max(vals) * 0.02, b.get_y() + b.get_height() / 2, f"{v}", va="center", fontsize=9.5)
    ax.set_title(f"{title}（{unit}）", fontsize=12)
    ax.grid(axis="x", color="#E5E5E5"); ax.grid(axis="y", visible=False)
    ax.set_xlim(0, max(vals) * 1.18)
axes[0].tick_params(axis="y", labelsize=9)
fig.suptitle("图2-2　主要液体火箭发动机推力与燃烧室压力对比", fontsize=14, fontweight="bold", y=1.0)
source_note(fig, "数据来源：SpaceX、蓝色起源、蓝箭航天、NPO Energomash、Aerojet Rocketdyne公开资料及航天媒体报道；为近似值，各型号不同批次参数有差异。\n猛禽3推力约280吨力、发动机本体约1,525公斤，推重比约180。")
save(fig, __file__)
