#!/usr/bin/env python3
"""Render the editable pitch outline as a compact, paginated reading PDF."""
from pathlib import Path
from html import escape
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'docs/pitch-structure.pdf'
BODY = ParagraphStyle('Body', fontName='Helvetica', fontSize=9.5,
                      leading=12.8, textColor=colors.HexColor('#243247'),
                      spaceAfter=5, alignment=TA_LEFT)
BULLET = ParagraphStyle('Bullet', parent=BODY, leftIndent=12, firstLineIndent=-9,
                        spaceAfter=3)
SECTION = ParagraphStyle('Section', parent=BODY, fontName='Helvetica-Bold',
                         fontSize=11.5, leading=15, spaceBefore=10, spaceAfter=6,
                         textColor=colors.HexColor('#163c68'), keepWithNext=True)
TITLE = ParagraphStyle('Title', parent=SECTION, fontSize=23, leading=28,
                       spaceBefore=0, spaceAfter=12)


def inline(text):
    text = text.replace('\u2014', '-').replace('\u2013', '-')
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1', text)
    return escape(text)


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor('#d7e1ed'))
    canvas.line(19 * mm, 17 * mm, 191 * mm, 17 * mm)
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(colors.HexColor('#52647a'))
    canvas.drawString(19 * mm, 12 * mm, 'pitch-sources-ivan | Editorial synthesis | 22 October 2026')
    canvas.drawRightString(191 * mm, 12 * mm, str(doc.page))
    canvas.restoreState()


def main():
    blocks = []
    section = []
    for line in (ROOT / 'docs/pitch-structure.md').read_text().splitlines():
        if line.startswith('# '):
            blocks.append(Paragraph(inline(line[2:]), TITLE))
        elif line.startswith('## '):
            if section:
                blocks.append(KeepTogether(section))
            section = [Paragraph(inline(line[3:]), SECTION)]
        elif line.startswith('- '):
            section.append(Paragraph('- ' + inline(line[2:]), BULLET))
        elif line.strip():
            (section if section else blocks).append(Paragraph(inline(line), BODY))
    if section:
        blocks.append(KeepTogether(section))
    doc = SimpleDocTemplate(str(OUTPUT), pagesize=(210 * mm, 297 * mm),
                            leftMargin=19 * mm, rightMargin=19 * mm,
                            topMargin=18 * mm, bottomMargin=24 * mm,
                            title='Startup pitch structure', author='pitch-sources-ivan',
                            subject='Early-stage pitch outline; separate hardware demo; no funding ask')
    doc.build(blocks, onFirstPage=footer, onLaterPages=footer)
    print(OUTPUT)


if __name__ == '__main__':
    main()
