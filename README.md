responsegen
==========

- **Copyright (c)** 2020 Julian Prester
- **License:** MIT
- **Description:** Small python script that drafts academic peer-review response sheets

## Features
- Parses PDF highlights into reviewer comments
- Uses highlight comment as initial response
- Uses underline annotation to separate different reviewers

## Usage
This is a script that extracts highlight annotations from a PDF file, and formats them as three-column table inside a Word document. It is intended for use in creating response sheets for received review packages.

For each annotation found in the PDF file, a row in the table is created, displaying the highlighted text and the text annotation, if any. Additionally, the annotations are numbered with a running index based on underline annotations.

The intended usage of this tool is to quickly draft response sheets based on a review package received as part of an academic peer-review process. When receiving a review package, I typically create a tabulated response sheet right away. I copy and paste reviewers' comments from my email client or PDF reader into a Word table, which serves as a resource for discussion with co-authors and issue tracker. When I've finished reading the paper, I use this script to convert the annotations to table in a Word document.

The description of the script is listed below.

### responsegen

```
usage: responsegen.py [-h] [-n COLS] INFILE [INFILE ...]

Extracts annotations from a PDF file in markdown format for use in revising.

positional arguments:
  INFILE                PDF files to process

optional arguments:
  -h, --help            show this help message and exit
  -n COLS, --cols COLS  number of columns per page in the document (default: 2)
```

## Similar projects
- [pdfannots](https://github.com/0xabu/pdfannots)
- [revision-sheet-generator](https://github.com/geritwagner/revision-sheet-generator)