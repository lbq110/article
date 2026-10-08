import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

tests = ["中国 2007.1\n风云一号C\n（约865公里）", "美国 2008.2\n USA-193\n（约247公里）", "印度 2019.3\nMicrosat-R\n（约283公里）", "俄罗斯 2021.11\n宇宙-1408\n（约480公里）"]
cat = [3530, 174, 125, 1780]
note = ["约3,530块\n目前仍有约2,300块在轨", "约174块\n最后一块2009年10月再入", "约125块\n2022年6月全部再入", "约1,780块\n多数已再入，残余或至2033年"]
fig, ax = plt.subplots(figsize=(8.6, 4.8))
cols = [ACCENT, PALETTE[0], PALETTE[3], PALETTE[4]]
bars = ax.bar(tests, cat, color=cols, width=0.56)
for b, t in zip(bars, note):
    ax.text(b.get_x() + b.get_width()/2, b.get_height() + 60, t, ha="center", va="bottom", fontsize=9)
ax.set_ylim(0, 4500)
ax.set_ylabel("可编目碎片数量（块）")
ax.set_title("图13-3　四次直接上升式反卫星试验产生的可编目碎片")
source_note(fig, "数据来源：CelesTrak/KeepTrack编目统计、McDowell、美国太空军（2022年AMOS会议）、Marco Langbroek（印度试验），均为约数；\n可编目碎片一般指地面可持续跟踪的约10厘米以上碎片，更小碎片数量高出1—2个数量级。高度越高，碎片滞留越久")
save(fig, __file__)
