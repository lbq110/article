import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

rows = [
    ("印度 曼加里安（2013）", 0.74, PALETTE[2]),
    ("阿联酋 希望号（2020）", 2.0, PALETTE[2]),
    ("美国 火星探路者（1996）", 2.65, PALETTE[0]),
    ("美国 MAVEN（2013）", 6.7, PALETTE[0]),
    ("美国 洞察号（2018）", 8.1, PALETTE[0]),
    ("美国 维京1/2号（1975）", 10.6, PALETTE[0]),
    ("美国 好奇号（2011）", 25, PALETTE[0]),
    ("美国 毅力号+机智号（2020）", 27, PALETTE[0]),
    ("NASA-ESA 火星采样返回\n（2023年独立评审估计，已终止）", 95, ACCENT),
]
fig, ax = plt.subplots(figsize=(9, 5.2))
y = list(range(len(rows)))[::-1]
ax.barh(y, [r[1] for r in rows], color=[r[2] for r in rows], height=0.58)
for yi, r in zip(y, rows):
    lab = "80—110" if r[1] == 95 else f"{r[1]:g}"
    ax.text(r[1] * 1.12, yi, lab, va="center", fontsize=10)
ax.set_xscale("log")
ax.set_xlim(0.4, 400)
ax.set_yticks(y); ax.set_yticklabels([r[0] for r in rows], fontsize=9.5)
ax.set_xticks([0.5, 1, 2, 5, 10, 20, 50, 100, 200])
ax.set_xticklabels(["0.5", "1", "2", "5", "10", "20", "50", "100", "200"])
ax.set_xlabel("任务成本（亿美元，名义值，对数坐标）")
ax.grid(axis="x", color="#E5E5E5"); ax.grid(axis="y", visible=False)
ax.set_title("典型火星任务成本对比：相差两个数量级")
source_note(fig, "数据来源：ISRO、阿联酋穆罕默德·本·拉希德航天中心、NASA任务资料及NASA火星采样返回独立评审委员会（IRB-2，2023）。均为名义美元，\n未作通胀调整（维京号若折算为今日美元远高于图中数值）；各任务口径（是否含发射、运行）不完全一致。天问一号未公开成本，未列入。")
save(fig, __file__)
