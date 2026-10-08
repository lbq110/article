import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

labels = ["设计2：成熟平面阵列\n（RD2，基准情形）", "设计1：创新定日镜群\n（RD1，基准情形）", "乐观组合情形\n（发射价减半+寿命翻倍+学习曲线）", "地面可再生能源\n（2050年预测，上限）", "地面可再生能源\n（2050年预测，下限）"]
vals = [1.59, 0.61, 0.03, 0.05, 0.02]
cols = [ACCENT, ACCENT, PALETTE[3], PALETTE[2], PALETTE[2]]
fig, ax = plt.subplots(figsize=(8.5, 4.6))
ax.grid(axis="x"); ax.grid(axis="y", visible=False)
y = list(range(len(vals)))[::-1]
ax.barh(y, vals, color=cols, height=0.6)
for yi, v in zip(y, vals):
    ax.text(v + 0.03, yi, f"{v:.2f} 美元/千瓦时", va="center", fontsize=9.5)
ax.set_yticks(y); ax.set_yticklabels(labels, fontsize=9.5)
ax.set_xlim(0, 2.0)
ax.set_xlabel("平准化度电成本（LCOE，美元/千瓦时）")
ax.set_title("图8-2　太空太阳能电站度电成本：NASA 2024年评估")
source_note(fig, "数据来源：NASA Office of Technology, Policy, and Strategy, Space-Based Solar Power（2024年1月）。两种参考设计均按2 GW规模、\n2050年运行情形测算；基准情形假设星舰单次发射价格1亿美元。")
save(fig, __file__)
