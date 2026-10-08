import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note
from matplotlib.lines import Line2D

# lane: 0=联合国条约/软法, 1=国家立法与监管, 2=多边/阵营性安排
events = [
    (1967, "《外层空间条约》", 0),
    (1968, "《营救协定》", 0),
    (1972, "《责任公约》", 0),
    (1975, "《登记公约》", 0),
    (1979, "《月球协定》（此后约20年无新的联合国空间条约）", 0),
    (2002, "IADC空间碎片减缓准则（“25年规则”）", 2),
    (2007, "联大核可联合国《空间碎片减缓准则》", 0),
    (2015, "美国《商业航天发射竞争法》（空间资源条款）", 1),
    (2017, "卢森堡《空间资源勘探和利用法》", 1),
    (2019, "外空委通过LTS准则（21条）；阿联酋联邦空间法", 0),
    (2020, "《阿尔忒弥斯协定》签署（首批8国）", 2),
    (2021, "日本《空间资源法》；中俄发布ILRS路线图", 1),
    (2022, "FCC“5年离轨”规则；美国宣布暂停DA-ASAT试验", 1),
    (2023, "ESA《零碎片宪章》；中国航天法列入立法规划", 2),
    (2025, "欧盟委员会提出《欧盟太空法》草案", 1),
]
names = {0: "联合国条约与软法", 1: "国家立法与监管", 2: "多边/俱乐部式安排"}
colors = {0: PALETTE[0], 1: PALETTE[1], 2: PALETTE[2]}

fig, ax = plt.subplots(figsize=(10, 6.2))
n = len(events)
for i, (yr, lab, lane) in enumerate(events):
    y = n - i
    ax.plot([1960, yr], [y, y], color="#EEEEEE", lw=0.8, zorder=1)
    ax.scatter(yr, y, s=60, color=colors[lane], zorder=3)
    ax.text(yr + 0.8, y, f"{yr}  {lab}", va="center", fontsize=9.2, color="#222222")
ax.axvspan(1980, 2001, color="#F4F4F4", zorder=0)
ax.text(1990.5, 2.3, "1980—2001：\n联合国层面\n“立法空窗期”", ha="center", fontsize=9, color="#777777")
ax.set_xlim(1960, 2065)
ax.set_ylim(0.3, n + 0.8)
ax.set_yticks([])
ax.set_xticks([1967, 1979, 1990, 2000, 2010, 2020])
ax.grid(False)
ax.spines["left"].set_visible(False)
handles = [Line2D([0], [0], marker="o", color="w", markerfacecolor=colors[k], markersize=9, label=v) for k, v in names.items()]
ax.legend(handles=handles, loc="upper right", fontsize=9.5, bbox_to_anchor=(1.0, 1.0))
ax.set_title("图12-1　太空规则演进时间线（1967—2025）")
source_note(fig, "数据来源：UNOOSA、IADC、美国国会、卢森堡政府公报、阿联酋航天局、FCC、ESA、欧盟委员会、全国人大常委会立法规划；作者整理")
save(fig, __file__)
