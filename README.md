# responsegen

## About

This is a Python script that extracts highlight annotations from a PDF file, and formats them as three-column table, and exports it to various formats.
It is intended for use in creating response sheets for academic journals.

For each annotation found in the PDF file, a row in the table is created, displaying the highlighted text and the text annotation, if any.
Additionally, the annotations are numbered with a running index based on underline annotations.

The intended usage of this tool is to quickly draft response sheets based on a review package received as part of an academic peer-review process.
When receiving a review package, I typically create a tabulated response sheet right away.
I copy and paste reviewers' comments from my email client or PDF reader into a Word table, which serves as a resource for discussion with co-authors and issue tracker.
When I've finished reading the paper, I use this script to convert the annotations to table in a Word document.

## Usage

```
usage: responsegen.py [-h] [-n COLS] INFILE [INFILE ...]

Extracts annotations from a PDF file in markdown format for use in revising.

positional arguments:
  INFILE                PDF files to process

optional arguments:
  -h, --help            show this help message and exit
  -n COLS, --cols COLS  number of columns per page in the document (default: 2)
```

## Roadmap

See the [open issues](https://github.com/julianprester/responsegen/issues) for a list of proposed features (and known issues).

## Built With

- [Python](https://www.python.org/)
- [Poetry](https://python-poetry.org/)
- [pdfminer.six](https://pdfminersix.readthedocs.io/en/latest/)
- [python-docx](https://python-docx.readthedocs.io/en/latest/)

## Support

Reach out to the maintainer at one of the following places:

- [GitHub issues](https://github.com/julianprester/responsegen/issues/new)
- The email which is located [on this website](https://julianprester.com)

## Contributing

First off, thanks for taking the time to contribute!
Contributions are what make the open-source community such an amazing place to learn, inspire, and create.
Any contributions you make will benefit everybody else and are **greatly appreciated**.

We have set up a separate document containing our [contribution guidelines](CONTRIBUTING.md).

Thank you for being involved!

## Authors & contributors

The original setup of this repository is by [Julian Prester](https://julianprester.com).

For a full list of all authors and contributors, check [the contributor's page](https://github.com/julianprester/responsegen/contributors).

## Security & Terms

Responsegen follows good practices of security, but 100% security can't be granted in software.
Responsegen is provided **"as is"** without any **warranty**. Use at your own risk.

## License

This project is licensed under the **MIT** license.

See [LICENSE](LICENSE) for more information.

## Acknowledgements

- [pdfannots](https://github.com/0xabu/pdfannots)
- [revision-sheet-generator](https://github.com/geritwagner/revision-sheet-generator)
