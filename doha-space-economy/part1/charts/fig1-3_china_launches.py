import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

labels = [str(y) for y in range(2015, 2026)] + ["2026\n上半年"]
vals = [19, 22, 18, 39, 34, 39, 55, 64, 67, 68, 92, 44]
fig, ax = plt.subplots(figsize=(8.5, 4.5))
cols = [PALETTE[0]] * 11 + [PALETTE[2]]
bars = ax.bar(labels, vals, color=cols, width=0.62)
for b, v in zip(bars, vals):
    ax.text(b.get_x() + b.get_width() / 2, v + 1.5, str(v), ha="center", fontsize=9.5)
ax.annotate("商业发射50次\n占54%", (10, 92), xytext=(7.3, 88), fontsize=9.5, color=ACCENT,
            arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
ax.annotate("商业发射30次\n占68.2%", (11, 44), xytext=(11, 66), fontsize=9.5, color=ACCENT, ha="center",
            arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
ax.set_ylabel("次")
ax.set_ylim(0, 105)
ax.set_title("图1-3　2015—2026年上半年中国航天发射次数（次）")
source_note(fig, "数据来源：国家航天局、中国航天科技集团年度发布，Jonathan McDowell发射日志；2026年上半年数据据澎湃新闻（2026年9月）。\n“商业发射”按国家航天局口径（含商业公司火箭及承揽商业载荷的发射）。")
save(fig, __file__)
