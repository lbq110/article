import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

periods = ["2022.12–\n2023.5", "2023.6–\n2023.11", "2023.12–\n2024.5", "2024.6–\n2024.11",
           "2024.12–\n2025.5", "2025.6–\n2025.11", "2025.12–\n2026.5"]
vals = [25299, 24410, 50000, 50666, 144404, 148696, 207152]
labels = ["25,299", "24,410", "约5万", "50,666", "144,404", "148,696", "207,152"]
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.bar(range(len(vals)), [v/10000 for v in vals], color=[PALETTE[0]]*4 + [ACCENT]*3, width=0.6)
for i, (v, l) in enumerate(zip(vals, labels)):
    ax.text(i, v/10000 + 0.4, l, ha="center", fontsize=9.5)
ax.set_xticks(range(len(vals))); ax.set_xticklabels(periods, fontsize=9.5)
ax.set_ylabel("避碰机动次数（万次）")
ax.set_ylim(0, 23.5)
ax.set_title("图7-5　星链卫星每半年避碰机动次数")
source_note(fig, "数据来源：SpaceX向FCC提交的半年度报告（经Space.com、Space Intel Report等转引）。\n2023年12月—2024年5月一期报道为“近5万次”，精确数未核实。")
save(fig, __file__)
