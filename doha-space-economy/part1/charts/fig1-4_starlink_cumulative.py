import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

labels = ["2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026.9"]
cum = [120, 950, 1950, 3680, 5650, 7650, 10850, 12962]
fig, ax = plt.subplots(figsize=(8.5, 4.5))
cols = [PALETTE[0]] * 7 + [ACCENT]
bars = ax.bar(labels, cum, color=cols, width=0.62)
for b, v in zip(bars, cum):
    ax.text(b.get_x() + b.get_width() / 2, v + 200, f"{v:,}" if v in (120, 12962) else f"约{v:,}",
            ha="center", fontsize=9.5)
ax.set_ylabel("颗（累计发射）")
ax.set_ylim(0, 14500)
ax.text(0, 11500, "2026年9月下旬：累计发射约12,960颗\n在轨约11,130颗，正常工作约11,120颗", fontsize=9.5, color="#444444")
ax.set_title("图1-4　星链卫星累计发射数量（年末，颗）")
source_note(fig, "数据来源：Jonathan McDowell星链统计（经Teal Group、Space.com、spaceweather.com、KeepTrack等转引）；\n2024、2025年末为按相邻时点数据推算的近似值；2026年9月为星舰第14次飞行后的星链状态统计。")
save(fig, __file__)
