import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note
import numpy as np

fig, ax = plt.subplots(figsize=(8.5, 4.8))
yrs = ["FY2021\n(申请)", "FY2022\n(申请)", "FY2023", "FY2024", "FY2025", "FY2026", "FY2027\n(申请)"]
base = [15.4, 17.5, 26.3, 28.9, 28.9, 26.135, 59.2]
recon = [0, 0, 0, 0, 0, 13.843, 12.1]
x = np.arange(len(yrs))
c = [GREY, GREY, PALETTE[0], PALETTE[0], PALETTE[0], PALETTE[0], ACCENT]
ax.bar(x, base, color=c, width=0.6, label="常规拨款（年度预算）")
ax.bar(x, recon, bottom=base, color=PALETTE[3], width=0.6, label="“和解法案”（强制性）资金")
for i in range(len(x)):
    t = base[i] + recon[i]
    ax.text(i, t + 1.2, f"{t:.1f}", ha="center", fontsize=10, fontweight="bold")
ax.set_xticks(x, yrs, fontsize=9.5)
ax.set_ylim(0, 80)
ax.set_ylabel("十亿美元")
ax.set_title("美国太空军预算（十亿美元）")
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=GREY, label="总统预算申请（早年）"), Patch(color=PALETTE[0], label="国会最终拨款（常规）"), Patch(color=PALETTE[3], label="“和解法案”（强制性）资金"), Patch(color=ACCENT, label="2027财年申请（常规部分）")], loc="upper left", fontsize=9)
source_note(fig, "数据来源：国会研究服务处（CRS）、SpacePolicyOnline、Taxpayers for Common Sense、CSIS/Aerospace预算简报；FY2021–22为总统预算申请数（灰色），\nFY2023–26为国会最终拨款数；FY2026另含《大而美法案》138亿美元；FY2027为2026年白宫申请（含121亿美元待和解法案）。不同统计口径略有差异。")
save(fig, __file__)
