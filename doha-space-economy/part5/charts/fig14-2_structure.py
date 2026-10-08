import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5), gridspec_kw={"width_ratios": [1, 1]})
# Left: Space Foundation 2024 vs 2025
labels = ["2024", "2025"]
comm = [480.3, 544.3]
us_gov = [77.3, 78.3]
other_gov = [55.0, 62.7]
x = np.arange(2)
ax1.bar(x, comm, color=PALETTE[0], width=0.55, label="商业收入")
ax1.bar(x, us_gov, bottom=comm, color=ACCENT, width=0.55, label="美国政府预算")
ax1.bar(x, other_gov, bottom=np.array(comm) + np.array(us_gov), color=PALETTE[3], width=0.55, label="其他国家政府预算")
for i in range(2):
    tot = comm[i] + us_gov[i] + other_gov[i]
    ax1.text(i, tot + 10, f"合计{tot:.0f}", ha="center", fontsize=10, fontweight="bold")
    ax1.text(i, comm[i] / 2, f"{comm[i]:.0f}\n({comm[i]/tot:.0%})", ha="center", color="white", fontsize=9.5)
ax1.set_xticks(x, labels)
ax1.set_ylim(0, 780)
ax1.set_title("商业与政府：Space Foundation口径", fontsize=12)
ax1.set_ylabel("十亿美元")
ax1.legend(fontsize=8.5, loc="upper left")
# Right: McKinsey/WEF backbone vs reach
yrs = ["2023", "2035（预测）"]
backbone = [330, 755]
reach = [300, 1045]  # 2035: "超过1万亿"，按1.8万亿-755推算
ax2.bar(x, backbone, color=PALETTE[2], width=0.55, label="“骨干”（backbone）：卫星、发射、通信与数据服务")
ax2.bar(x, reach, bottom=backbone, color=PALETTE[4], width=0.55, label="“延伸”（reach）：太空赋能的行业收入")
for i in range(2):
    ax2.text(i, backbone[i] / 2, f"{backbone[i]}", ha="center", color="white", fontsize=10)
    ax2.text(i, backbone[i] + reach[i] / 2, f"{reach[i]:,}" if i == 0 else "1,000以上", ha="center", color="white", fontsize=10)
    ax2.text(i, backbone[i] + reach[i] + 25, f"合计{backbone[i]+reach[i]:,}" if i == 0 else "合计约1,800", ha="center", fontsize=10, fontweight="bold")
ax2.set_xticks(x, yrs)
ax2.set_ylim(0, 2350)
ax2.set_title("骨干与延伸：麦肯锡/WEF口径", fontsize=12)
ax2.legend(fontsize=8.5, loc="upper left")
fig.suptitle("图解太空经济的结构（十亿美元）", fontsize=14, fontweight="bold", y=1.02)
source_note(fig, "数据来源：Space Foundation《The Space Report》2025 Q2（2024年）与2026年7月发布（2025年，其他国家政府预算=1410-783亿美元推算）；\n世界经济论坛/麦肯锡《Space: The $1.8 Trillion Opportunity for Global Economic Growth》（2024年4月）；2035年\u201c延伸\u201d原文为\u201c超过1万亿\u201d，柱高按1.8万亿减755推算。")
save(fig, __file__)
