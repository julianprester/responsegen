import fitz
from highlight import Highlight


def extract_highlights(file_name):
    doc = fitz.open(file_name)
    highlights = []
    for page in doc:
        for annot in page.annots(types=[fitz.PDF_ANNOT_HIGHLIGHT, fitz.PDF_ANNOT_UNDERLINE]):
            min_y, min_x = sorted(annot.vertices)[0]
            highlight = extract_annotation(annot, page)
            highlights.append(Highlight(annot.info["id"], annot.info["subject"], highlight, annot.info["content"], annot.info["title"], page.number+1, min_x, min_y))
    doc.close()
    sortedHighlights = sorted(highlights, key=lambda highlight: (highlight.page, highlight.x, highlight.y))
    return sortedHighlights

def extract_annotation(annot, page):
    highlights = []
    for i in range(0, len(annot.vertices), 4):
        r = fitz.Quad(annot.vertices[i : i + 4]).rect
        rcX, rcY = (r.x0 + r.width / 2), (r.y0 + r.height / 2)
        m = fitz.Matrix(1, 0, 0, 1, -rcX, -rcY)
        m.concat(m, fitz.Matrix(1.01, 1.01))
        m.concat(m, fitz.Matrix(1, 0, 0, 1, rcX, rcY))

        r = r.transform(m)

        highlights.append(page.get_textbox(r))
    return ' '.join(highlights)
