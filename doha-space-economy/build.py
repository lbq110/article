"""Assemble all parts into one Word document.

    python3 build.py            # -> dist/外太空经济_多哈演讲底稿.docx (+ .md)

Steps: (re)render every chart, concatenate 00_front.md + part*/**.md with image
paths rewritten to be relative to this folder, run pandoc with a Chinese
reference.docx, then fix up fonts / image alignment with python-docx.
"""
import pathlib
import re
import subprocess
import sys

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

ROOT = pathlib.Path(__file__).resolve().parent
DIST = ROOT / "dist"
NAME = "外太空经济_多哈演讲底稿"

BODY_FONT, HEAD_FONT, LATIN = "宋体", "黑体", "Times New Roman"


def render_charts():
    for script in sorted(ROOT.glob("part*/charts/*.py")):
        r = subprocess.run([sys.executable, "-I", str(script)], capture_output=True, text=True)
        if r.returncode:
            sys.exit(f"chart failed: {script}\n{r.stderr}")


def assemble():
    chunks = [(ROOT / "00_front.md").read_text(encoding="utf-8")]
    for part in sorted(ROOT.glob("part[1-5]")):
        for md in sorted(part.glob("*.md")):
            text = md.read_text(encoding="utf-8")
            text = re.sub(r"\]\(charts/", f"](" + part.name + "/charts/", text)
            text = re.sub(r"\]\(\.\./source/", "](source/", text)
            chunks.append(text.strip() + "\n")
    return "\n\n".join(chunks)


def _set_font(style, east, latin, size=None, bold=None, color=None):
    style.font.name = latin
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = rpr.makeelement(qn("w:rFonts"), {})
        rpr.append(rfonts)
    for k in ("w:ascii", "w:hAnsi", "w:cs"):
        rfonts.set(qn(k), latin)
    rfonts.set(qn("w:eastAsia"), east)
    for k in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
        rfonts.attrib.pop(qn(k), None)
    if size:
        style.font.size = Pt(size)
    if bold is not None:
        style.font.bold = bold
    if color is not None:
        style.font.color.rgb = RGBColor.from_string(color)


def make_reference(path):
    default = DIST / "_pandoc_default_ref.docx"
    with open(default, "wb") as f:
        subprocess.run(["pandoc", "--print-default-data-file", "reference.docx"], stdout=f, check=True)
    doc = Document(default)
    st = {s.name: s for s in doc.styles}  # by literal name (python-docx remaps "Heading 1")
    for name in ("Normal", "Body Text", "First Paragraph", "Compact"):
        s = st[name]
        _set_font(s, BODY_FONT, LATIN, 11.5)
        pf = s.paragraph_format
        pf.line_spacing = 1.5
        pf.space_after = Pt(6)
        if name in ("Body Text", "First Paragraph"):
            pf.first_line_indent = Pt(23)
    sizes = {"TOC Heading": 20, "Title": 26, "Subtitle": 15, "Heading 1": 20, "Heading 2": 16, "Heading 3": 13.5, "Heading 4": 12}
    for name, size in sizes.items():
        _set_font(st[name], HEAD_FONT, "Arial", size, bold=True, color="1F4E79")
        st[name].paragraph_format.space_before = Pt(18 if name in ("Heading 1", "Heading 2") else 10)
        st[name].paragraph_format.space_after = Pt(8)
    st["Heading 1"].paragraph_format.page_break_before = True
    st["Heading 1"].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for name in ("Image Caption", "Table Caption"):
        _set_font(st[name], HEAD_FONT, "Arial", 10, bold=False, color="404040")
        st[name].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        st[name].font.italic = False
    _set_font(st["Date"], BODY_FONT, LATIN, 12)
    for sec in doc.sections:
        sec.page_height, sec.page_width = Cm(29.7), Cm(21.0)
        sec.left_margin = sec.right_margin = Cm(2.5)
        sec.top_margin = sec.bottom_margin = Cm(2.5)
    doc.save(path)


def postprocess(path):
    doc = Document(path)
    for p in doc.paragraphs:
        # centre paragraphs that only hold a picture, drop their first-line indent
        if p._p.xpath(".//w:drawing") and not p.text.strip():
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.first_line_indent = Pt(0)
        # bold "表x-x" captions written as their own paragraph
        if re.match(r"^表\d+-\d+", p.text.strip()):
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.first_line_indent = Pt(0)
            p.paragraph_format.keep_with_next = True
    for t in doc.tables:
        t.style = next(s for s in doc.styles if s.name == "Table")
        t.alignment = 1
        for row in t.rows:
            for cell in row.cells:
                for p in cell.paragraphs:
                    p.paragraph_format.first_line_indent = Pt(0)
                    p.paragraph_format.line_spacing = 1.15
                    for r in p.runs:
                        r.font.size = Pt(9.5)
        # visible borders
        tblPr = t._tbl.tblPr
        borders = tblPr.makeelement(qn("w:tblBorders"), {})
        for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
            borders.append(borders.makeelement(qn(f"w:{edge}"), {
                qn("w:val"): "single", qn("w:sz"): "4", qn("w:color"): "A6A6A6"}))
        for old in tblPr.findall(qn("w:tblBorders")):
            tblPr.remove(old)
        tblPr.append(borders)
    doc.save(path)


def main():
    DIST.mkdir(exist_ok=True)
    render_charts()
    md = DIST / f"{NAME}.md"
    md.write_text(assemble(), encoding="utf-8")
    ref = DIST / "_reference.docx"
    make_reference(ref)
    out = DIST / f"{NAME}.docx"
    subprocess.run([
        "pandoc", str(md), "-o", str(out),
        "--from", "markdown+pipe_tables+implicit_figures-tex_math_dollars",
        "--reference-doc", str(ref), "--resource-path", str(ROOT),
        "--toc", "--toc-depth=2", "-M", "toc-title=目录",
    ], check=True, cwd=ROOT)
    postprocess(out)
    for tmp in (ref, DIST / "_pandoc_default_ref.docx"):
        tmp.unlink()
    print("built", out)


if __name__ == "__main__":
    main()
