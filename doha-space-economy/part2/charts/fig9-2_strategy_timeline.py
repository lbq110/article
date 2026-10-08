import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note
from matplotlib.lines import Line2D

colors = {"中国": ACCENT, "美国": PALETTE[0], "欧洲": PALETTE[2], "印度": PALETTE[3], "日韩": PALETTE[4], "海湾": PALETTE[7], "卢森堡": GREY}
ev = [
    ("美国", 2015.9, "美国《商业航天发射竞争法》确认企业对所获太空资源的权利"),
    ("卢森堡", 2017.6, "卢森堡《太空资源探索与利用法》生效"),
    ("海湾", 2019.2, "阿联酋发布《国家太空战略2030》"),
    ("美国", 2019.97, "美国太空军成立"),
    ("印度", 2020.45, "印度设立IN-SPACe，向私营部门开放"),
    ("中国", 2020.6, "北斗三号全球系统建成开通"),
    ("美国", 2020.8, "《阿尔忒弥斯协定》首批8国签署（含阿联酋）"),
    ("海湾", 2021.1, "阿联酋“希望号”进入火星轨道"),
    ("印度", 2023.3, "《印度空间政策2023》发布"),
    ("海湾", 2023.4, "沙特两名宇航员进入国际空间站"),
    ("日韩", 2023.9, "日本设立10年1万亿日元宇宙战略基金"),
    ("日韩", 2024.4, "韩国航天航空厅（KASA）成立"),
    ("欧洲", 2024.95, "欧盟IRIS²星座特许合同签署"),
    ("欧洲", 2025.48, "欧盟委员会提出《欧盟太空法》草案"),
    ("中国", 2025.9, "国家航天局印发商业航天行动计划（2025—2027年）"),
    ("欧洲", 2025.9, "ESA部长级会议：三年约221亿欧元"),
    ("美国", 2026.0, "FCC追加批准7500颗星链Gen2卫星"),
    ("美国", 2026.3, "阿尔忒弥斯2号载人绕月成功"),
    ("中国", 2030.0, "中国载人登月目标"),
    ("印度", 2035.0, "印度空间站（BAS）建成目标"),
]
fig, ax = plt.subplots(figsize=(10.5, 7))
ax.grid(axis="x"); ax.grid(axis="y", visible=False)
n = len(ev)
for i, (c, x, lab) in enumerate(ev):
    y = n - 1 - i
    done = x <= 2026.77
    ax.plot([2014.5, x], [y, y], color="#F0F0F0", lw=1, zorder=0)
    ax.plot(x, y, "o", ms=8, color=colors[c] if done else "white", mec=colors[c], mew=2, zorder=3)
    if x < 2029:
        ax.text(x + 0.3, y, lab, va="center", ha="left", fontsize=8.8)
    else:
        ax.text(x - 0.3, y, lab, va="center", ha="right", fontsize=8.8)
ax.axvline(2026.77, color=GREY, ls="--", lw=1)
ax.set_yticks([]); ax.spines["left"].set_visible(False)
ax.set_xlim(2014.5, 2036.5); ax.set_ylim(-0.8, n)
ax.set_xticks(range(2015, 2037, 3))
handles = [Line2D([], [], marker="o", ls="", color=v, ms=8, label=k) for k, v in colors.items()]
ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.08), ncol=8, fontsize=9)
ax.set_title("图9-2　主要国家和地区太空战略关键节点（实心=已发生，空心=目标）")
source_note(fig, "数据来源：国家航天局、新华社、NASA、FCC、欧盟委员会、ESA、ISRO/IN-SPACe、日本内阁府、韩国KASA、阿联酋航天局、沙特航天局、卢森堡政府等公开信息。作者整理。")
save(fig, __file__)
