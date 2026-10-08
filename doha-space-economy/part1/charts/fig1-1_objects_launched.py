import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))
from chartstyle import plt, PALETTE, ACCENT, GREY, save, source_note

# UNOOSA Online Index via Our World in Data (World series). 1957-2022: OWID snapshot (TidyTuesday 2024-04-23 mirror);
# 2023 revised to 2,903 and 2025 = 4,510 per OWID data insight / Yale e360 (2026).
# 2024: UN value not retrieved; Space Foundation count of spacecraft deployed (2,802) shown as a hatched bar.
owid = {1957:2,1958:8,1959:14,1960:20,1961:38,1962:77,1963:71,1964:107,1965:163,1966:145,1967:159,1968:140,1969:138,
1970:130,1971:156,1972:133,1973:138,1974:128,1975:158,1976:158,1977:137,1978:165,1979:124,1980:130,1981:158,1982:145,
1983:154,1984:163,1985:165,1986:134,1987:135,1988:145,1989:139,1990:168,1991:135,1992:130,1993:108,1994:123,1995:105,
1996:100,1997:152,1998:157,1999:129,2000:121,2001:86,2002:96,2003:88,2004:74,2005:72,2006:95,2007:111,2008:109,
2009:125,2010:120,2011:129,2012:134,2013:210,2014:241,2015:222,2016:221,2017:456,2018:454,2019:586,2020:1274,
2021:1813,2022:2478,2023:2903,2025:4510}
years = sorted(owid)
fig, ax = plt.subplots(figsize=(9, 4.8))
ax.bar(years, [owid[y] for y in years], width=0.8, color=PALETTE[0])
ax.bar([2024], [2802], width=0.8, color="white", edgecolor=PALETTE[0], hatch="////", linewidth=0.8)
ax.set_xlim(1955, 2027)
ax.set_ylabel("个")
for y, txt, xy in [(2019, "2019年：586", (2005, 836)), (2023, "2023年：2,903", (2004, 3400)), (2025, "2025年：4,510", (2012, 4300))]:
    v = owid[y]
    ax.annotate(txt, (y, v), xytext=xy, fontsize=9.5,
                arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
ax.annotate("2024年：约2,800\n（Space Foundation口径，斜线柱）", (2024, 2802), xytext=(1998, 2150), fontsize=9,
            color="#444444", arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
ax.text(1960, 900, "1957—2016年：每年约100—250个\n“国家工程”时代的平台期", fontsize=9.5, color="#444444")
ax.set_title("图1-1　1957—2025年全球每年送入太空的物体数量（个）")
source_note(fig, "数据来源：联合国外空司（UNOOSA）在轨物体登记索引，经Our World in Data整理（2023、2025年为2026年修订值）；\n2024年为Space Foundation《The Space Report 2024 Q4》航天器部署数。UN登记约覆盖实际发射物体的88%。")
save(fig, __file__)
