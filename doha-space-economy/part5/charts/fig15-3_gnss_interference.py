import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.5, 4.6), gridspec_kw={"width_ratios": [1.2, 1]})
yrs = ["2023", "2024", "2025\n(截至8月28日)"]
v = [55, 495, 733]
b = ax1.bar(yrs, v, color=[PALETTE[0], PALETTE[0], ACCENT], width=0.55)
for bb, vv in zip(b, v):
    ax1.text(bb.get_x() + bb.get_width()/2, vv + 15, str(vv), ha="center", fontsize=11, fontweight="bold")
ax1.set_ylim(0, 850)
ax1.set_title("瑞典交通局记录的GNSS干扰事件（起）", fontsize=12)
ax2.axis("off")
txt = ("波罗的海地区（2025年1–4月）\n\n"
       "约 123,000 架次航班\n受源自俄罗斯的GNSS干扰影响\n\n"
       "涉及 365 家航空公司\n\n"
       "4月份平均 27.4% 的航班\n遭遇干扰")
ax2.text(0.5, 0.5, txt, ha="center", va="center", fontsize=12, linespacing=1.4,
         bbox=dict(boxstyle="round,pad=0.8", fc="#F3F6FA", ec=PALETTE[0]))
fig.suptitle("卫星导航干扰正在常态化", fontsize=14, fontweight="bold", y=1.02)
source_note(fig, "数据来源：瑞典交通局（Transportstyrelsen）数据经乌克兰新闻社等转引；波罗的海三国向国际民航组织（ICAO）提交的报告，经瑞典电视台SVT、\n爱沙尼亚公共广播ERR报道（2025年）。")
save(fig, __file__)
