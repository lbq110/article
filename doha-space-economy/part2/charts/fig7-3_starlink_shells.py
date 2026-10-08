import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note
from matplotlib.patches import Patch

# rows ordered by altitude (high -> low): label, count or None, color, note
rows = [
    ("570 km · 倾角70°", 720, PALETTE[0], "720颗"),
    ("560 km · 倾角97.6°（极轨）", 520, PALETTE[0], "520颗"),
    ("550 km · 倾角53°", 1584, PALETTE[0], "1,584颗"),
    ("540 km · 倾角53.2°", 1584, PALETTE[0], "1,584颗"),
    ("525/530/535 km · 倾角53°/43°/33°", 7500, PALETTE[2], "合计7,500颗（Gen2首批）"),
    ("475–485 km（2026年新增壳层）", None, PALETTE[3], "约4,400颗卫星由550 km降至约480 km（2026年内）"),
    ("340–365 km（2026年新增甚低轨壳层）", None, PALETTE[3], "Gen2第二批7,500颗的部分壳层"),
    ("约275 km（V3首批入轨高度）", None, ACCENT, "星舰第14次飞行部署26颗V3，随后自行升轨"),
]
fig, ax = plt.subplots(figsize=(9, 5))
ax.grid(axis="x"); ax.grid(axis="y", visible=False)
ys = list(range(len(rows)))[::-1]
for y, (lab, n, c, note) in zip(ys, rows):
    if n:
        ax.barh(y, n, height=0.6, color=c)
        ax.text(n + 80, y, note, va="center", fontsize=9)
    else:
        ax.barh(y, 200, height=0.6, color=c, alpha=0.5)
        ax.text(280, y, note, va="center", fontsize=9, color="#333333")
ax.set_yticks(ys); ax.set_yticklabels([r[0] for r in rows], fontsize=9.5)
ax.set_xlim(0, 10000)
ax.set_xlabel("FCC授权卫星数（颗）")
ax.legend(handles=[Patch(color=PALETTE[0], label="第一代（Gen1）合计4,408颗"),
                   Patch(color=PALETTE[2], label="第二代首批（2022年12月）"),
                   Patch(color=PALETTE[3], alpha=0.5, label="2026年调整/新增（数量未分壳层公布）")],
          loc="lower right", fontsize=8.8)
ax.set_title("图7-3　星链主要轨道壳层（按高度由高到低）")
source_note(fig, "数据来源：FCC授权文件（2020年修改许可、2022年12月Gen2许可、2026年1月9日Gen2追加许可）；SpaceX工程副总裁Michael Nicolls 2026年1月1日公告；\n星舰第14次飞行报道（2026年9月28日）。作者整理。")
save(fig, __file__)
