"""Word-style character count for Chinese manuscripts.

Counts CJK characters + CJK punctuation + each run of Latin letters/digits as 1
(roughly what Microsoft Word reports as 字数). Image lines, HTML comments and
table rule lines are excluded.

    python3 common/wordcount.py part1/*.md
"""
import re
import sys

CJK = re.compile(r"[㐀-鿿豈-﫿　-〿＀-￯‘-”…—]")
WORD = re.compile(r"[A-Za-z0-9][A-Za-z0-9.\-%]*")


def count(text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    lines = [l for l in text.splitlines()
             if not l.strip().startswith("![") and not re.fullmatch(r"[\s|:\-+=]*", l)]
    text = "\n".join(lines)
    return len(CJK.findall(text)) + len(WORD.findall(text))


if __name__ == "__main__":
    total = 0
    for p in sys.argv[1:]:
        n = count(open(p, encoding="utf-8").read())
        total += n
        print(f"{n:>7}  {p}")
    print(f"{total:>7}  TOTAL")
