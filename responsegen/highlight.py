from docx.oxml.ns import nsdecls
from docx.oxml import parse_xml
from pydantic import BaseModel
from datetime import datetime
import fitz

class Highlight(BaseModel):
    type: int
    text: str
    comment: str
    author: str
    date: datetime
    page: int
    x: int
    y: int

    def to_csv(self, numbering):
        if self.type == fitz.PDF_ANNOT_HIGHLIGHT:
            return [numbering, self.text, self.comment]
        if self.type == fitz.PDF_ANNOT_UNDERLINE:
            return ['', f'**{self.text.capitalize()} comments**', '']

    def to_md(self, numbering):
        if self.type == fitz.PDF_ANNOT_HIGHLIGHT:
            return f"| {numbering} | {self.text} | {self.comment} |\n"
        if self.type == fitz.PDF_ANNOT_UNDERLINE:
            return f"| | **{self.text.capitalize()} comments** | |\n"

    def to_docx(self, numbering, row):
        if self.type == fitz.PDF_ANNOT_HIGHLIGHT:
            row[0].text = f"{numbering}"
            row[1].text = self.text
            row[2].text = self.comment
            return row
        if self.type == fitz.PDF_ANNOT_UNDERLINE:
            merged = row[1].merge(row[2])
            merged.text = self.text.capitalize() + " comments"
            shading_elm_0 = parse_xml(r'<w:shd {} w:fill="000000"/>'.format(nsdecls('w')))
            row[0]._tc.get_or_add_tcPr().append(shading_elm_0)
            shading_elm_1 = parse_xml(r'<w:shd {} w:fill="000000"/>'.format(nsdecls('w')))
            merged._tc.get_or_add_tcPr().append(shading_elm_1)
            return row