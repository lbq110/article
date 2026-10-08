# 第二轮事实核查（通用说明）

你负责核查《外太空经济》某一部分中"未能核实/请作者确认"的事项，并直接修订书稿。

- 工作目录：/home/user/article/doha-space-economy；先读 common/BRIEF.md（总纲）、本部分 partN/zz_notes.md（待确认清单），再按需读相关章节。
- WebSearch / WebFetch 需先用 ToolSearch 查询 "select:WebSearch,WebFetch" 加载。**本轮全部核查代理共享200次检索额度，你最多用35次 WebSearch**，自己计数，优先核查对演讲影响最大的事项（时效性新闻、核心数字）。WebFetch 很多站点被网络代理拦截，失败就不要反复重试。
- 今天是2026-10-08。只采信可靠来源；查不到就保持原文的审慎表述，不要编造。
- 修订方式：
  1. 正文数字或说法有误/可更新 → 直接改 partN/chNN.md 对应句子，必要时同步改 partN/charts/ 下的图表脚本数据并重新运行（`python3 -I partN/charts/xxx.py`），用 Read 看一眼PNG确认无重叠。图表样式由 common/chartstyle.py 统一控制，不要改它。
  2. 更新 partN/zz_notes.md："数据核查说明"中把已核实的条目改为"已核实（第二轮）→ 结论 → 来源"；仍查不到的保留在"请作者确认"清单。
  3. 字数保持在 20,000–22,300（`python3 common/wordcount.py partN/*.md`），新增内容要相应精简。
- 只改本部分目录；不要 git commit。
- 最终回复（给主控，简洁，中文）：用了几次检索；每个事项的核查结论（已改/确认无误/仍未核实）；改了哪些文件和图表；当前字数。
