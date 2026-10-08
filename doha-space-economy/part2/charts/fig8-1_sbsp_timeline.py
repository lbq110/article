import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note
from matplotlib.lines import Line2D

colors = {"美国": PALETTE[0], "中国": ACCENT, "欧洲": PALETTE[2], "日本": PALETTE[4], "英国": PALETTE[3]}
# (country, year, label, done)
ev = [
    ("日本", 2015.2, "日本：JAXA与J-spacesystems地面微波传能试验（约55米）", True),
    ("中国", 2022.5, "中国：重庆璧山空间太阳能电站地面试验基地复工", True),
    ("欧洲", 2022.9, "欧洲：ESA部长级会议批准SOLARIS预研", True),
    ("美国", 2023.2, "美国：加州理工SSPD-1首次在轨无线能量传输", True),
    ("美国", 2024.0, "美国：NASA OTPS评估——2050年成本仍远高于地面", True),
    ("欧洲", 2025.9, "欧洲：SOLARIS原定就是否进入全面开发作出决策", True),
    ("日本", 2026.5, "日本：OHISAMA小卫星在轨传能演示（计划FY2026）", False),
    ("中国", 2028.0, "中国：低轨10千瓦级无线传能试验（2022年规划）", False),
    ("中国", 2030.0, "中国：兆瓦级在轨试验（2026年报道仍为2030年前后）", False),
    ("英国", 2030.0, "英国：Space Solar在轨演示（公司目标）", False),
    ("中国", 2050.0, "中国：2吉瓦级空间电站（远期目标）", False),
]
fig, ax = plt.subplots(figsize=(10, 5.4))
ax.grid(axis="x"); ax.grid(axis="y", visible=False)
n = len(ev)
for i, (c, x, lab, done) in enumerate(ev):
    y = n - 1 - i
    ax.plot([2013, x], [y, y], color="#EEEEEE", lw=1, zorder=0)
    ax.plot(x, y, "o", ms=9, color=colors[c] if done else "white", mec=colors[c], mew=2, zorder=3)
    ax.text(x + 0.6 if x < 2040 else x - 0.6, y, lab, va="center", ha="left" if x < 2040 else "right", fontsize=9)
ax.axvline(2026.77, color=GREY, ls="--", lw=1)
ax.text(2026.9, n - 0.4, "2026年10月", fontsize=8.5, color=GREY)
ax.set_yticks([]); ax.spines["left"].set_visible(False)
ax.set_xlim(2013, 2052); ax.set_ylim(-0.8, n)
ax.set_xticks([2015, 2020, 2025, 2030, 2035, 2040, 2045, 2050])
handles = [Line2D([], [], marker="o", ls="", color=v, ms=8, label=k) for k, v in colors.items()]
ax.legend(handles=handles, loc="upper right", ncol=1, fontsize=9)
ax.set_title("图8-1　太空太阳能电站：主要里程碑与计划（实心=已发生，空心=计划）")
source_note(fig, "数据来源：Caltech（2023）；NASA OTPS《Space-Based Solar Power》（2024）；ESA SOLARIS项目页；南华早报、Aviation Week等对中国计划的报道（2021—2022）；人民日报、新华社（2026）；\nJAXA/J-spacesystems（2025）；Space Solar公司公开信息。计划节点均为相关机构公布的目标，可能调整。")
save(fig, __file__)
