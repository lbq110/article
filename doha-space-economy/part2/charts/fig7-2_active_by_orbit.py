import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

cats = ["低地球轨道\n（LEO，含SSO）", "地球同步类轨道\n（GEO/IGSO）", "中地球轨道\n（MEO）", "大椭圆/甚高轨道\n（HEO/VHEO）", "其他"]
vals = [13661, 572, 268, 22, 14]
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.grid(axis="x"); ax.grid(axis="y", visible=False)
y = range(len(cats))[::-1]
bars = ax.barh(list(y), vals, color=[PALETTE[0], PALETTE[4], PALETTE[2], PALETTE[3], GREY], height=0.6)
ax.set_xscale("log")
ax.set_xlim(8, 60000)
ax.set_yticks(list(y)); ax.set_yticklabels(cats)
total = sum(vals)
for yi, v in zip(y, vals):
    ax.text(v * 1.15, yi, f"{v:,}（{v/total:.1%}）", va="center", fontsize=10)
ax.set_xlabel("在轨活跃卫星数量（颗，对数刻度）")
ax.set_title("图7-2　在轨活跃卫星按轨道类型分布（2026年2月）")
source_note(fig, "数据来源：Jonathan McDowell, Jonathan's Space Pages（数据截至2026年2月7日；LEO合并LLEO/LSSO/SSO等子类）。")
save(fig, __file__)
