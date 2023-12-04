from docx.oxml.ns import nsdecls
from docx.oxml import parse_xml

SUBSTITUTIONS = {
    u'ﬀ': 'ff',
    u'ﬁ': 'fi',
    u'ﬂ': 'fl',
    u'ﬃ': 'ffi',
    u'ﬄ': 'ffl',
    u'‘': "'",
    u'’': "'",
    u'“': '"',
    u'”': '"',
    u'…': '...',
}

class Highlight:
    def __init__(self, id, type, text, comment, author, page, x, y):
        self.id = id
        self.type = type
        self.text = ''.join([SUBSTITUTIONS.get(c, c) for c in text.strip()])
        self.comment = comment
        self.author = author
        self.page = page
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.id} - {self.type} - {self.text} - {self.comment} - {self.author}"

    def to_csv(self, numbering):
        if self.type == "Highlight":
            return [numbering, self.text, self.comment]
        if self.type == "Underline":
            return ['', f'**{self.text.capitalize()} comments**', '']

    def to_md(self, numbering):
        if self.type == "Highlight":
            return f"| {numbering} | {self.text} | {self.comment} |\n"
        if self.type == "Underline":
            return f"| | **{self.text.capitalize()} comments** | |\n"

    def to_docx(self, numbering, row):
        if self.type == "Highlight":
            row[0].text = f"{numbering}"
            row[1].text = self.text
            row[2].text = self.comment
            return row
        if self.type == "Underline":
            merged = row[1].merge(row[2])
            merged.text = self.text.capitalize() + " comments"
            shading_elm_0 = parse_xml(r'<w:shd {} w:fill="000000"/>'.format(nsdecls('w')))
            row[0]._tc.get_or_add_tcPr().append(shading_elm_0)
            shading_elm_1 = parse_xml(r'<w:shd {} w:fill="000000"/>'.format(nsdecls('w')))
            merged._tc.get_or_add_tcPr().append(shading_elm_1)
            return row