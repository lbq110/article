import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.6), gridspec_kw={"width_ratios": [1.5, 1]})

# 左：项目总投入（十亿美元）
items = ["阿波罗计划 1960—1973\n（名义值）", "阿波罗计划\n（折合2025年美元）", "阿尔忒弥斯 2012—2025财年\n（OIG估算，名义值）", "“月球基地”计划 2026—2032\n（NASA宣布，名义值）"]
vals = [25.8, 309, 93, 20]
cols = [GREY, PALETTE[3], PALETTE[0], PALETTE[2]]
y = list(range(len(items)))[::-1]
ax1.barh(y, vals, color=cols, height=0.55)
for yi, v in zip(y, vals):
    ax1.text(v + 5, yi, f"{v:g}", va="center", fontsize=10)
ax1.set_yticks(y); ax1.set_yticklabels(items, fontsize=9)
ax1.set_xlim(0, 360)
ax1.grid(axis="x", color="#E5E5E5"); ax1.grid(axis="y", visible=False)
ax1.set_title("项目投入（十亿美元）", fontsize=12)

# 右：NASA预算占联邦预算比重
labs = ["1966财年\n（阿波罗高峰）", "2024财年"]
share = [4.41, 0.37]
ax2.bar(labs, share, color=[PALETTE[3], PALETTE[0]], width=0.5)
for i, v in enumerate(share):
    ax2.text(i, v + 0.1, f"{v}%", ha="center", fontsize=11)
ax2.set_ylim(0, 5.2)
ax2.set_title("NASA预算占联邦支出比重", fontsize=12)
fig.suptitle("阿波罗与阿尔忒弥斯：投入规模对比", fontsize=14, fontweight="bold", y=1.03)
fig.tight_layout()
source_note(fig, "数据来源：美国行星协会（阿波罗258亿美元，折合2025年约3090亿美元）；NASA监察长办公室IG-22-003（2021）；NASA 2026年3月“Ignition”发布会；\n美国白宫管理与预算办公室历史表。2024财年按NASA拨款约249亿美元、联邦支出约6.75万亿美元计算。各口径不完全可比。")
save(fig, __file__)
