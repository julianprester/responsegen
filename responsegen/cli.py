import click

from responsegen.extract import extract_highlights
from responsegen.export import export

@click.command()
@click.option('-f', '--format', default="docx", help='choose file format (csv, md, docx)')
@click.option('-o', '--output', help='output file to write to')
@click.argument('FILE')
def main(format, output, file):
    """Extracts annotations from a PDF file for use in creating a response sheet to an academic paper revision."""
    highlights = extract_highlights(file)
    if output:
        out_file = output
    else:
        file_name = file[:file.rindex(".")]
        out_file = f"{file_name}.{format}"
    export(highlights, out_file, format)

if __name__ == "__main__":
    main()