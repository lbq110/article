import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(figsize=(10, 4.6))
ax.set_xlim(-1.2, 15.4); ax.set_ylim(-2.15, 1.5)
ax.axis("off")
# main arrow
ax.annotate("", xy=(15, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color="#444444", lw=1.6))
# phases
ax.add_patch(FancyBboxPatch((0, 0.12), 7, 0.5, boxstyle="round,pad=0.02", color=PALETTE[0], alpha=0.9))
ax.text(3.5, 0.37, "规定期限：7年内“投入使用”（BIU）", ha="center", va="center", color="white", fontsize=10.5, fontweight="bold")
ax.add_patch(FancyBboxPatch((7, 0.12), 7, 0.5, boxstyle="round,pad=0.02", color=PALETTE[3], alpha=0.95))
ax.text(10.5, 0.37, "第35号决议（WRC-19）里程碑期：再给7年", ha="center", va="center", color="white", fontsize=10.5, fontweight="bold")
pts = [
    (0, "第0年\n主管部门向ITU提交\n资料（API/协调请求）\n——“排队号”起算", PALETTE[0]),
    (7, "第7年\n至少1颗卫星进入申报\n轨道面并连续运行90天\n（M0：投入使用）", PALETTE[0]),
    (9, "第9年（7+2）\nM1：部署10%", ACCENT),
    (12, "第12年（7+5）\nM2：部署50%", ACCENT),
    (14, "第14年（7+7）\nM3：部署100%", ACCENT),
]
for i, (x, lab, c) in enumerate(pts):
    ax.plot([x, x], [-0.15, 0.12], color=c, lw=2)
    ax.scatter(x, 0, s=70, color=c, zorder=5)
    if x <= 7:
        ax.text(x, -0.3, lab, ha="center", va="top", fontsize=9.2, color="#222222")
    else:
        ax.text(x, 0.8, lab, ha="center", va="bottom", fontsize=9.2, color=ACCENT)
ax.text(9.6, -1.15, "未达标后果：\nM1未达标→登记数量上限降为已部署数×10\nM2未达标→降为已部署数×2\nM3未达标→降至实际部署数",
        ha="left", va="center", fontsize=9.6, color=ACCENT)
ax.text(7.1, -2.0, "两种常见说法其实是同一规则：“申报后7/9/12/14年”是从申报日算；“7年后再2/5/7年”是从BIU期限届满算",
        ha="center", fontsize=9.2, color="#444444")
ax.set_title("图13-1　ITU非静止轨道星座“里程碑”规则时间轴")
source_note(fig, "数据来源：ITU《无线电规则》第11.44款、第35号决议（WRC-19通过，WRC-23修订）及ITU 2024年区域研讨会材料；作者绘制")
save(fig, __file__)
