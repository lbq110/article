import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

years = ["2020", "2021", "2022", "2023", "2024", "2025", "2026\n(至9月25日)"]
cum = [9, 14, 23, 33, 52, 59, 76]
new = [9, 5, 9, 10, 19, 7, 17]
fig, ax = plt.subplots(figsize=(8.6, 4.8))
bars = ax.bar(years, cum, color=PALETTE[0], width=0.6, label="累计签署国")
ax.bar(years, new, color=PALETTE[3], width=0.6, label="当年新增")
for b, c, n in zip(bars, cum, new):
    ax.text(b.get_x() + b.get_width() / 2, c + 1.2, str(c), ha="center", fontsize=11, fontweight="bold")
    ax.text(b.get_x() + b.get_width() / 2, n / 2, f"+{n}", ha="center", va="center", fontsize=9, color="white")
ax.annotate("海湾/阿拉伯国家：\n阿联酋2020（创始）、巴林2022.3、\n沙特2022.7、阿曼2026.1、约旦2026.4", xy=(0.2, 11.5), xytext=(-0.3, 40),
            fontsize=8.8, color="#333333", arrowprops=dict(arrowstyle="->", color=GREY))
ax.set_ylim(0, 85)
ax.set_ylabel("国家数（个）")
ax.legend(loc="upper left")
ax.set_title("图12-3　《阿尔忒弥斯协定》签署国数量（2020—2026）")
source_note(fig, "数据来源：NASA、美国国务院公告；年末累计数（2026年为截至9月25日圣马力诺签署时的76国）；作者整理")
save(fig, __file__)
