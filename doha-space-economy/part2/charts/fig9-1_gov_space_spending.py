import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

fig, axes = plt.subplots(1, 2, figsize=(10, 4.6), gridspec_kw={"width_ratios": [1.1, 1]})
ax = axes[0]
years = ["2024年", "2025年"]
defense = [73.0, 73.5]; civil = [62.0, 63.7]
ax.bar(range(2), defense, color=PALETTE[0], width=0.5, label="国防")
ax.bar(range(2), civil, bottom=defense, color=PALETTE[2], width=0.5, label="民用")
for i in range(2):
    ax.text(i, defense[i]/2, f"{defense[i]:.1f}", ha="center", color="white", fontsize=10)
    ax.text(i, defense[i] + civil[i]/2, f"{civil[i]:.1f}", ha="center", color="white", fontsize=10)
    ax.text(i, defense[i] + civil[i] + 2, f"合计约{defense[i]+civil[i]:.0f}" if i == 0 else "合计137.4", ha="center", fontsize=10)
ax.set_xticks(range(2)); ax.set_xticklabels(years)
ax.set_ylim(0, 160); ax.set_ylabel("十亿美元")
ax.legend(loc="upper left", ncol=2, fontsize=9.5)
ax.set_title("全球政府航天支出：国防占54%", fontsize=12)
ax = axes[1]
labs = ["美国", "中国", "其他国家\n和机构"]
vals = [79.7, 19.0, 135 - 79.7 - 19.0]
ax.barh([2, 1, 0], vals, color=[PALETTE[0], ACCENT, GREY], height=0.55)
ax.set_yticks([2, 1, 0]); ax.set_yticklabels(labs)
txt = ["约797亿（59%）", "190亿以上（约14%）", "约363亿（约27%）"]
for yv, v, t in zip([2, 1, 0], vals, txt):
    ax.text(v + 1.5, yv, t, va="center", fontsize=9.5)
ax.set_xlim(0, 120); ax.grid(axis="x"); ax.grid(axis="y", visible=False)
ax.set_xlabel("十亿美元（2024年）")
ax.set_title("2024年国别结构", fontsize=12)
fig.suptitle("图9-1　全球政府航天支出规模与结构", fontsize=14, fontweight="bold", y=1.03)
source_note(fig, "数据来源：Novaspace《Government Space Programs》第24版（2024年数据）、第25版（2025年数据）新闻稿；国别数据经Statista转引。\n中国为外部机构估算（中国未公布完整航天预算），“其他”为作者按总额倒算，均为约数。")
save(fig, __file__)
