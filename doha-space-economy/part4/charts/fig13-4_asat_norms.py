import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.4), gridspec_kw={"width_ratios": [1.15, 1]})
# Left: UNGA 77/41 vote
cats = ["赞成", "反对", "弃权", "未投票"]
vals = [155, 9, 9, 20]
cols = [PALETTE[0], ACCENT, PALETTE[3], GREY]
b = ax1.bar(cats, vals, color=cols, width=0.6)
for bb, v in zip(b, vals):
    ax1.text(bb.get_x() + bb.get_width()/2, v + 3, str(v), ha="center", fontsize=11, fontweight="bold")
ax1.set_ylim(0, 180)
ax1.set_ylabel("国家数（个）")
ax1.set_title("联大第77/41号决议表决（2022.12.7）", fontsize=11.5)
ax1.text(1.9, 52, "反对（9）：白俄罗斯、玻利维亚、中非、中国、\n古巴、伊朗、尼加拉瓜、俄罗斯、叙利亚\n弃权（9）：印度、巴基斯坦、老挝、马达加斯加、\n塞尔维亚、斯里兰卡、苏丹、多哥、津巴布韦", ha="center", fontsize=8.2, color="#444444")
# Right: unilateral pledges cumulative
dates = ["2022.4\n美国首倡", "2023.4", "2025.1"]
nums = [1, 13, 38]
ax2.plot(dates, nums, marker="o", color=PALETTE[2], lw=2.2)
for x, v in zip(dates, nums):
    ax2.text(x, v + 2, str(v), ha="center", fontsize=11, fontweight="bold")
ax2.set_ylim(0, 48)
ax2.set_ylabel("作出承诺的国家（累计，个）")
ax2.set_title("承诺不进行破坏性DA-ASAT试验的国家", fontsize=11.5)
fig.suptitle("图13-4　禁止破坏性反卫星试验：联大投票与各国单边承诺", fontsize=14, fontweight="bold", y=1.03)
fig.tight_layout()
source_note(fig, "数据来源：联合国数字图书馆A/RES/77/41表决记录、SpacePolicyOnline；安全世界基金会（SWF）多边空间安全倡议追踪（2025年1月：美国之外另有37国）；\n四个做过此类试验的国家中，仅美国作出承诺")
save(fig, __file__)
