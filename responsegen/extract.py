import fitz
from datetime import datetime
from responsegen.highlight import Highlight

fitz.TOOLS.set_small_glyph_heights(True)

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

def extract_highlights(file_name):
    doc = fitz.open(file_name)
    highlights = []
    for page in doc:
        for annot in page.annots(types=[fitz.PDF_ANNOT_HIGHLIGHT, fitz.PDF_ANNOT_UNDERLINE]):
            highlight = extract_annotation(annot, page)
            highlights.append(highlight)
    doc.close()
    sortedHighlights = sorted(highlights, key=lambda highlight: (highlight.page, highlight.y, highlight.x))
    return sortedHighlights

def extract_annotation(annot, page):
    quad_count = int(len(annot.vertices) / 4)
    sentences = ["" for i in range(quad_count)]
    for i in range(quad_count):
        points = annot.vertices[i * 4 : i * 4 + 4]
        sentences[i] = page.get_text(clip=fitz.Quad(points).rect + (-1, 0, 1, 0))
    sentences = " ".join(sentences)
    sentences = ''.join([SUBSTITUTIONS.get(c, c) for c in sentences.strip()])
    sentences = sentences.replace("\n ", " ")
    return Highlight(
        type=annot.type[0],
        text=sentences,
        comment=annot.info["content"],
        author=annot.info["title"],
        date=datetime.strptime(annot.info["modDate"][2:-1], '%Y%m%d%H%M%S'),
        page=page.number+1,
        x=sorted(annot.vertices)[0][0],
        y=sorted(annot.vertices)[0][1]
    )
