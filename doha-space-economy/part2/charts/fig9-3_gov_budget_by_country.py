import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

# Novaspace《Government Space Programs》第24版，2024年政府航天支出（十亿美元，经Statista转引）
# GDP：IMF《世界经济展望》2025年4月版，2024年名义GDP（十亿美元）；占比为作者计算
rows = [  # 名称, 支出, GDP（欧盟为机构预算，不计算占比）
    ("美国", 79.7, 29185),
    ("中国", 19.9, 18748),
    ("日本", 6.8, 4026),
    ("欧盟（机构）", 6.7, None),
    ("俄罗斯", 4.0, 2161),
    ("法国", 3.7, 3162),
    ("德国", 2.8, 4660),
    ("意大利", 2.6, 2373),
]
names = [r[0] for r in rows]
y = list(range(len(rows)))[::-1]
fig, axes = plt.subplots(1, 2, figsize=(10, 5), gridspec_kw={"width_ratios": [1.25, 1]})

ax = axes[0]
cols = [PALETTE[0], ACCENT] + [PALETTE[2]] * 6
ax.barh(y, [r[1] for r in rows], color=cols, height=0.6)
for yi, r in zip(y, rows):
    ax.text(r[1] + 1.2, yi, f"{r[1]:.1f}", va="center", fontsize=10)
ax.set_yticks(y); ax.set_yticklabels(names)
ax.set_xlim(0, 92)
ax.grid(axis="x"); ax.grid(axis="y", visible=False)
ax.set_xlabel("十亿美元（2024年）")
ax.set_title("政府航天支出", fontsize=12)

ax = axes[1]
shares = [(r[1] / r[2] * 100) if r[2] else None for r in rows]
for yi, s, c in zip(y, shares, cols):
    if s is None:
        ax.text(0.005, yi, "不适用", va="center", fontsize=9.5, color=GREY)
        continue
    ax.barh(yi, s, color=c, height=0.6)
    ax.text(s + 0.006, yi, f"{s:.2f}%", va="center", fontsize=10)
ax.set_yticks(y); ax.set_yticklabels([])
ax.set_xlim(0, 0.34)
ax.grid(axis="x"); ax.grid(axis="y", visible=False)
ax.set_xlabel("占本国GDP比重（%）")
ax.set_title("投入强度：占GDP比重", fontsize=12)

fig.suptitle("图9-3　主要国家和地区政府航天支出及占GDP比重（2024年）", fontsize=14, fontweight="bold", y=1.02)
source_note(fig, "数据来源：支出为Novaspace《Government Space Programs》第24版（经Statista转引），含民用与国防；中国为外部估算。\n"
                 "GDP为IMF《世界经济展望》2025年4月版2024年名义值，占比为作者计算。欧洲各国与欧盟机构的数字口径可能交叉，不宜相加。")
save(fig, __file__)
