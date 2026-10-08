import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note
import datetime as dt
import matplotlib.dates as mdates

# 近似的地火霍曼转移发射窗口（各约1—2个月）与火星冲日日期
windows = [
    ("2026-11-01", "2026-12-31", "2027-02-19"),
    ("2028-11-25", "2029-01-31", "2029-03-25"),
    ("2031-01-15", "2031-03-31", "2031-05-04"),
    ("2033-03-15", "2033-05-15", "2033-06-27"),
    ("2035-05-10", "2035-07-20", "2035-09-15"),
]
d = lambda s: dt.datetime.strptime(s, "%Y-%m-%d")
fig, ax = plt.subplots(figsize=(10, 3.6))
for i, (a, b, opp) in enumerate(windows):
    ax.barh(1, (d(b) - d(a)).days, left=d(a), height=0.42, color=PALETTE[3])
    ax.scatter(d(opp), 0.35, marker="v", color=ACCENT, s=50, zorder=3)
    mid = d(a) + (d(b) - d(a)) / 2
    ax.text(mid, 1.33, f"{d(a).year}年{d(a).month}月—\n{d(b).year}年{d(b).month}月", ha="center", va="bottom", fontsize=9)
    ax.text(d(opp), 0.12, f"冲日\n{d(opp).year}.{d(opp).month:02d}", ha="center", va="top", fontsize=8.5, color="#444444")
    if i < len(windows) - 1:
        nxt = d(windows[i + 1][0])
        ax.annotate("", xy=(nxt, 0.75), xytext=(d(b), 0.75),
                    arrowprops=dict(arrowstyle="<->", color=GREY, lw=0.9))
        ax.text(d(b) + (nxt - d(b)) / 2, 0.8, "约26个月", ha="center", va="bottom", fontsize=8.5, color="#666666")
ax.set_ylim(-0.6, 2.1)
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.grid(False)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
ax.set_xlim(d("2026-01-01"), d("2036-01-01"))
ax.set_title("2026—2035年地火转移发射窗口（橙色）与火星冲日（▼）")
source_note(fig, "数据来源：火星冲日日期据NASA/天文年历；发射窗口为霍曼型转移的近似区间（作者据冲日前约2—4个月的规律估算），具体窗口因任务能量需求不同而异。")
save(fig, __file__)
