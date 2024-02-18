import csv
from docx import Document
from docx.shared import Inches
import fitz

def export(highlights, filename, format):
    if format == "docx":
        export_docx(highlights, filename)
    if format == "md":
        export_md(highlights, filename)
    if format == "csv":
        export_csv(highlights, filename)

def export_csv(highlights, filename):
    with open(filename, "w", encoding='utf-8', newline='') as f:
        csvwriter = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        csvwriter.writerow(['','Editor/Reviewer Comments', 'Response'])
        reviewer = ""
        counter = 0
        for highlight in highlights:
            if highlight.type == fitz.PDF_ANNOT_UNDERLINE:
                reviewer = highlight.comment if highlight.comment else highlight.text
                reviewer += "."
                counter = 0
            csvwriter.writerow(highlight.to_csv(f"{reviewer}{counter}"))
            counter += 1

def export_md(highlights, filename):
    with open(filename, "w", encoding='utf-8') as f:
        f.write("| | Editor/Reviewer Comments | Response |\n")
        f.write("| --- | --- | --- |\n")
        reviewer = ""
        counter = 0
        for highlight in highlights:
            if highlight.type == fitz.PDF_ANNOT_UNDERLINE:
                reviewer = highlight.comment if highlight.comment else highlight.text
                reviewer += "."
                counter = 0
            f.write(highlight.to_md(f"{reviewer}{counter}"))
            counter += 1

def export_docx(highlights, filename):
    document = Document()
    table = document.add_table(rows=(len(highlights) + 1), cols=3)
    table.style = 'Table Grid'
    widths = (Inches(0.32), Inches(4.5), Inches(4.5))
    for row in table.rows:
        for idx, width in enumerate(widths):
            row.cells[idx].width = width
    heading_cells = table.rows[0].cells
    heading_cells[1].text = 'Editor/Reviewer Comments'
    heading_cells[2].text = 'Response'
    reviewer = ""
    counter = 0
    for key, highlight in enumerate(highlights):
        if highlight.type == fitz.PDF_ANNOT_UNDERLINE:
            reviewer = highlight.comment if highlight.comment else highlight.text
            reviewer += "."
            counter = 0
        row = table.rows[key + 1].cells
        row = highlight.to_docx(f"{reviewer}{counter}", row)
        counter += 1
    document.save(filename)