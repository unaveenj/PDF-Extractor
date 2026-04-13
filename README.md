# PDF Page Extractor

A simple command-line tool to extract a range of pages from a PDF file and save them as a new PDF.

## Features

- Interactive prompts for PDF path, page range, and output filename
- Validates input at every step (file existence, page bounds, empty values)
- Saves the extracted pages to the same directory as the source PDF

## Requirements

- Python 3.7+
- [pypdf](https://pypdf.readthedocs.io/) 4.3.1

## Installation

```bash
# Clone the repository
git clone https://github.com/unaveenj/PDF-Extractor.git
cd PDF-Extractor

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python extract_pdf.py
```

You will be prompted to:

1. Enter the path to your PDF file
2. Specify the start and end page numbers to extract
3. Enter a name for the output file

The extracted PDF is saved in the same directory as the source file.

## Example

```
=== PDF Page Extractor ===

Enter the path to the PDF file: /Users/naveen/Documents/report.pdf

  'report.pdf' has 42 page(s).

Page range to extract:
  Start page (1–42): 5
  End page (5–42): 10

Enter output file name (without .pdf): report_pages_5_to_10

Extracting pages...

Done! Extracted 6 page(s) to:
  /Users/naveen/Documents/report_pages_5_to_10.pdf
```

## Project Structure

```
PDF-Extractor/
├── extract_pdf.py    # Main script
├── requirements.txt  # Python dependencies
└── README.md
```

## License

This project is open source and available under the [MIT License](LICENSE).
>>>>>>> 567d607 (Initial commit: PDF page extractor with README)
