import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note
import numpy as np

regions = ["欧洲", "美洲", "亚太", "中东/西亚", "非洲"]
# Artemis signatories at end-2025 (59), classified by author from NASA/State Dept list
artemis = [28, 12, 10, 5, 4]
# ILRS state partners per public reports (13 incl. China & Russia); Azerbaijan counted as West Asia (like Armenia), Egypt as Africa
ilrs = [3, 2, 4, 1, 3]
y = np.arange(len(regions))
h = 0.38
fig, ax = plt.subplots(figsize=(8.6, 4.8))
b1 = ax.barh(y - h/2, artemis, h, color=PALETTE[0], label="《阿尔忒弥斯协定》签署国（2025年底，59国）")
b2 = ax.barh(y + h/2, ilrs, h, color=ACCENT, label="国际月球科研站（ILRS）国家伙伴（13国）")
for bars in (b1, b2):
    for b in bars:
        w = b.get_width()
        ax.text(w + 0.4, b.get_y() + b.get_height()/2, f"{int(w)}", va="center", fontsize=10)
ax.set_yticks(y)
ax.set_yticklabels(regions)
ax.invert_yaxis()
ax.grid(axis="x", color="#E5E5E5"); ax.grid(axis="y", visible=False)
ax.set_xlabel("国家数（个）")
ax.set_xlim(0, 33)
ax.legend(loc="lower right", fontsize=9.5)
ax.text(32.5, 1.1, "两边都参加：泰国、塞内加尔\n（另有阿联酋沙迦大学等机构\n以非国家身份加入ILRS）", ha="right", fontsize=8.8, color="#444444")
ax.set_title("图12-4　两种月球规则“朋友圈”的地区构成")
source_note(fig, "数据来源：NASA/美国国务院签署名单（截至2025年12月，59国，作者按地区归类：中东/西亚含阿联酋、以色列、巴林、沙特、亚美尼亚）；\nILRS国家伙伴据中国国家航天局与SpaceNews等报道（含中俄13国，阿塞拜疆计入西亚）；中方口径为17个国家和国际组织（2025年4月）")
save(fig, __file__)
