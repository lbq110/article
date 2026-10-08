import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

# 2013-2026 年（截至2026年10月）全部月面软着陆尝试
# result: S=成功, P=着陆但姿态异常/部分成功, F=失败
missions = [
    ("2013.12", "嫦娥三号", "中国", "国家", "S"),
    ("2019.01", "嫦娥四号", "中国", "国家", "S"),
    ("2019.04", "创世纪号", "以色列SpaceIL", "商业", "F"),
    ("2019.09", "月船2号维克拉姆", "印度", "国家", "F"),
    ("2020.12", "嫦娥五号", "中国", "国家", "S"),
    ("2023.04", "HAKUTO-R M1", "日本ispace", "商业", "F"),
    ("2023.08", "月球25号", "俄罗斯", "国家", "F"),
    ("2023.08", "月船3号", "印度", "国家", "S"),
    ("2024.01", "游隼号（未抵月）", "美国Astrobotic", "商业", "F"),
    ("2024.01", "SLIM", "日本JAXA", "国家", "P"),
    ("2024.02", "IM-1奥德修斯", "美国直觉机器", "商业", "P"),
    ("2024.06", "嫦娥六号", "中国", "国家", "S"),
    ("2025.03", "蓝色幽灵M1", "美国萤火虫", "商业", "S"),
    ("2025.03", "IM-2雅典娜", "美国直觉机器", "商业", "P"),
    ("2025.06", "Resilience(M2)", "日本ispace", "商业", "F"),
]
colors = {"S": PALETTE[0], "P": PALETTE[3], "F": ACCENT}
labels = {"S": "成功", "P": "部分成功（着陆后姿态异常）", "F": "失败"}

fig, ax = plt.subplots(figsize=(9, 6.2))
n = len(missions)
for i, (d, name, who, kind, r) in enumerate(missions):
    y = n - 1 - i
    marker = "o" if kind == "国家" else "s"
    ax.axhline(y, xmin=0.02, xmax=0.98, color="#EEEEEE", lw=0.8, zorder=0)
    ax.text(0.0, y, d, ha="left", va="center", fontsize=9.5, color="#555555")
    ax.text(0.55, y, name, ha="left", va="center", fontsize=10)
    ax.text(1.75, y, who, ha="left", va="center", fontsize=9.5, color="#444444")
    ax.text(2.75, y, kind, ha="left", va="center", fontsize=9.5, color="#444444")
    ax.scatter(3.35, y, s=110, marker=marker, color=colors[r], zorder=3)
    ax.text(3.5, y, labels[r], ha="left", va="center", fontsize=9.5)
for x, h in [(0.0, "时间"), (0.55, "任务"), (1.75, "国家/机构"), (2.75, "类型"), (3.35, "结果")]:
    ax.text(x, n, h, ha="left" if x != 3.35 else "center", va="center", fontsize=10, fontweight="bold")
ax.set_xlim(-0.05, 4.3)
ax.set_ylim(-0.8, n + 0.6)
ax.axis("off")
from matplotlib.patches import Patch
handles = [Patch(color=colors[k], label=labels[k]) for k in ["S", "P", "F"]]
ax.set_title("2013—2026年全球月面软着陆尝试结果（共15次）")
ax.text(0.0, -0.9, "国家任务8次：成功5、部分成功1、失败2；商业任务7次：成功1、部分成功2、失败4。圆点=国家任务，方块=商业任务。",
         ha="left", va="top", fontsize=9.5, color="#333333")
source_note(fig, "数据来源：NASA、CNSA、ISRO、JAXA及各公司公告，作者整理。截至2026年10月，2026年内无新的月面着陆尝试；\n游隼号因推进剂泄漏未能抵达月球，计为失败。")
save(fig, __file__)
