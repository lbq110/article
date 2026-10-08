import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note
import numpy as np

rows = [
    # name, filed (ITU), deployed in orbit (latest), note
    ("卢旺达 Cinnamon-217/937\n（2021年申报）", 327320, None),
    ("中国 CTC-1/CTC-2\n（2025年12月申报）", 193428, None),
    ("SpaceX 星链\n（一代+二代）", 42000, 10900),
    ("中国 千帆（垣信）", 14000, 238),
    ("中国 国网（GW）", 12992, 204),
    ("中国 鸿鹄-3（蓝箭关联）", 10000, None),
    ("亚马逊 Leo（柯伊伯）", 3236, 396),
]
names = [r[0] for r in rows]
filed = [r[1] for r in rows]
dep = [r[2] for r in rows]
y = np.arange(len(rows))
h = 0.38
fig, ax = plt.subplots(figsize=(9.2, 5.4))
ax.barh(y - h/2, filed, h, color=GREY, label="向ITU申报/拟建数量")
dep_vals = [d if d else 0 for d in dep]
ax.barh(y + h/2, [d if d else np.nan for d in dep], h, color=PALETTE[0], label="实际在轨数量（2026年最新）")
ax.set_xscale("log")
ax.set_xlim(80, 2_000_000)
for i, (f, d) in enumerate(zip(filed, dep)):
    ax.text(f * 1.12, i - h/2, f"{f:,}", va="center", fontsize=9)
    if d:
        ax.text(d * 1.12, i + h/2, f"{d:,}（{d/f:.1%}）", va="center", fontsize=9, color=PALETTE[0])
    else:
        ax.text(95, i + h/2, "尚无入轨", va="center", fontsize=9, color=ACCENT)
ax.set_yticks(y); ax.set_yticklabels(names, fontsize=9.5)
ax.invert_yaxis()
ax.grid(axis="x", color="#E5E5E5", which="major"); ax.grid(axis="y", visible=False)
ax.set_xlabel("卫星数量（颗，对数坐标）")
ax.legend(loc="lower right", fontsize=9.5)
ax.set_title("图13-2　主要低轨星座：ITU申报数与实际部署数（对数坐标）")
source_note(fig, "数据来源：ITU卫星网络数据库及相关报道（卢旺达、CTC、鸿鹄-3、国网、千帆申报数）；星链在轨约10,900颗（KeepTrack，2026年8月5日）；\n亚马逊Leo 396颗（2026年7月2日发射后）；国网低轨组网星204颗（截至2026年9月，公开统计）；千帆238颗（上海垣信，2026年7月9日）；\n星链申报数为约数（一代约1.2万+二代约3万）；括号内为部署数/申报数")
save(fig, __file__)
