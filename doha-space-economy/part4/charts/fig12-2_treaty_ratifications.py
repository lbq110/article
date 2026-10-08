import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

treaties = ["《外层空间条约》\n(1967)", "《营救协定》\n(1968)", "《责任公约》\n(1972)", "《登记公约》\n(1975)", "《月球协定》\n(1979)"]
ratified = [118, 100, 100, 78, 17]
labels = ["118", "100", "100", "约78", "17"]
fig, ax = plt.subplots(figsize=(8.6, 4.8))
cols = [PALETTE[0]] * 4 + [ACCENT]
bars = ax.bar(treaties, ratified, color=cols, width=0.58)
for b, t in zip(bars, labels):
    ax.text(b.get_x() + b.get_width() / 2, b.get_height() + 3, t, ha="center", fontsize=11, fontweight="bold")
ax.axhline(193, color=GREY, ls="--", lw=1)
ax.text(4.35, 186, "联合国会员国 193", ha="right", va="top", fontsize=9, color="#555555")
ax.annotate("美、俄、中均未加入；\n沙特2024年1月退出", xy=(4, 24), xytext=(4, 62), ha="center", fontsize=9, color=ACCENT,
            arrowprops=dict(arrowstyle="->", color=ACCENT))
ax.set_ylim(0, 205)
ax.set_ylabel("缔约国数量（个）")
ax.set_title("图12-2　联合国五大外空条约缔约国数量（截至2025年底—2026年初）")
source_note(fig, "数据来源：UNOOSA《与外空活动有关的国际协定现况》（截至2025年1月1日及2026年1月1日版）、联合国裁军事务厅（马来西亚2025年10月成为OST第118个缔约国）；\n《登记公约》2025年1月1日为76国，此后厄瓜多尔等加入，2026年初约78国")
save(fig, __file__)
