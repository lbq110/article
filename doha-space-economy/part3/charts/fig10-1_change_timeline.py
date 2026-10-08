import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

# (年份小数, 名称, 说明, 阶段, 状态)
events = [
    (2007.81, "嫦娥一号", "首次绕月", "绕", "done"),
    (2010.75, "嫦娥二号", "7米分辨率全月图", "绕", "done"),
    (2013.95, "嫦娥三号", "首次软着陆+玉兔", "落", "done"),
    (2018.38, "鹊桥", "地月L2中继", "落", "done"),
    (2019.01, "嫦娥四号", "人类首次月背着陆", "落", "done"),
    (2020.96, "嫦娥五号", "带回1731克", "回", "done"),
    (2024.22, "鹊桥二号", "新一代中继星", "四期", "done"),
    (2024.48, "嫦娥六号", "月背采样1935.3克", "回", "done"),
    (2027.6, "嫦娥七号", "南极资源勘查\n（2026年8月推迟）", "四期", "plan"),
    (2029.2, "嫦娥八号", "原位资源利用试验\n（约2029年）", "四期", "plan"),
    (2029.9, "载人登月", "2030年前", "载人", "plan"),
    (2035.0, "ILRS基本型", "约2035年", "四期", "plan"),
]
stage_color = {"绕": PALETTE[2], "落": PALETTE[0], "回": PALETTE[3], "四期": PALETTE[4], "载人": ACCENT}

fig, ax = plt.subplots(figsize=(10, 4.8))
ax.axhline(0, color="#555555", lw=1.2, zorder=1)
offsets = [1.0, -1.0, 1.6, -1.7, 0.95, -1.0, 1.7, -1.75, 1.0, -1.0, 1.75, -1.05]
for (x, name, note, stage, st), dy in zip(events, offsets):
    c = stage_color[stage]
    ax.plot([x, x], [0, dy * 0.82], color=c, lw=1, zorder=1)
    ax.scatter(x, 0, s=60, color=c if st == "done" else "white", edgecolor=c, linewidth=1.8, zorder=3)
    va = "bottom" if dy > 0 else "top"
    ax.text(x, dy * 0.85, f"{name}\n{note}", ha="center", va=va, fontsize=8.6,
            color="#222222" if st == "done" else "#555555")
ax.set_ylim(-2.45, 2.6)
ax.set_xlim(2006.3, 2036.5)
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax.grid(False)
ax.set_xticks(range(2007, 2037, 3))
from matplotlib.lines import Line2D
handles = [Line2D([], [], marker="o", ls="", color=stage_color[k], label=l, markersize=7)
           for k, l in [("绕", "一期“绕”"), ("落", "二期“落”"), ("回", "三期“回”"), ("四期", "四期/科研站"), ("载人", "载人登月")]]
handles.append(Line2D([], [], marker="o", ls="", markerfacecolor="white", markeredgecolor=GREY, label="空心=计划中", markersize=7))
ax.legend(handles=handles, loc="upper left", ncol=6, fontsize=8.6, bbox_to_anchor=(0, 1.06))
ax.set_title("中国探月工程任务时间轴（2007—2035年）", pad=22)
source_note(fig, "数据来源：国家航天局（CNSA）、中国载人航天工程办公室公告；计划节点为官方公布的预期时间，嫦娥七号新发射时间以官方公告为准。")
save(fig, __file__)
