import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

fig, ax = plt.subplots(figsize=(8.5, 4.6))
items = [
    ("国会已拨付（2025年和解法案）", 25, GREY),
    ("2027财年申请额", 17.5, GREY),
    ("特朗普宣布（2025年5月）", 175, PALETTE[0]),
    ("项目负责人Guetlein：至2035年“目标架构”", 185, PALETTE[0]),
    ("CBO：去掉天基层的方案（20年）", 448, PALETTE[3]),
    ("CBO：含约7800颗卫星天基层（20年）", 1200, ACCENT),
]
items = items[::-1]
labels = [i[0] for i in items]; vals = [i[1] for i in items]; cols = [i[2] for i in items]
bars = ax.barh(labels, vals, color=cols, height=0.6)
for b, v in zip(bars, vals):
    ax.text(v + 15, b.get_y() + b.get_height()/2, f"{v:,.1f}".rstrip("0").rstrip("."), va="center", fontsize=10)
ax.set_xlim(0, 1400)
ax.grid(axis="x", color="#E5E5E5"); ax.grid(axis="y", visible=False)
ax.set_xlabel("十亿美元")
ax.set_title("“金穹”导弹防御计划：不同口径的成本数字（十亿美元）")
source_note(fig, "数据来源：美国国会预算办公室（CBO，2026年5月12日，“示意性方案”估算）；Breaking Defense、Defense One、Air & Space Forces等对Guetlein证词及\n2027财年预算的报道；白宫2025年5月20日声明。注：各数字口径不同（研发/部署/20年运维），不可直接比较。")
save(fig, __file__)
