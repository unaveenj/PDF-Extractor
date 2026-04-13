import os
import sys
from pypdf import PdfReader, PdfWriter


def prompt_pdf_path():
    while True:
        path = input("Enter the path to the PDF file: ").strip()
        if not path:
            print("  Path cannot be empty.")
            continue
        if not os.path.isfile(path):
            print(f"  File not found: {path}")
            continue
        if not path.lower().endswith(".pdf"):
            print("  File does not appear to be a PDF.")
            continue
        return path


def prompt_page_range(total_pages):
    while True:
        try:
            start = int(input(f"  Start page (1–{total_pages}): "))
            if not (1 <= start <= total_pages):
                print(f"  Must be between 1 and {total_pages}.")
                continue
            break
        except ValueError:
            print("  Please enter a valid number.")

    while True:
        try:
            end = int(input(f"  End page ({start}–{total_pages}): "))
            if not (start <= end <= total_pages):
                print(f"  Must be between {start} and {total_pages}.")
                continue
            break
        except ValueError:
            print("  Please enter a valid number.")

    return start, end


def prompt_output_name():
    while True:
        name = input("Enter output file name (without .pdf): ").strip()
        if not name:
            print("  Name cannot be empty.")
            continue
        if not name.endswith(".pdf"):
            name += ".pdf"
        return name


def extract_pages(input_path, start_page, end_page, output_name):
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for i in range(start_page - 1, end_page):
        writer.add_page(reader.pages[i])

    output_dir = os.path.dirname(os.path.abspath(input_path))
    output_path = os.path.join(output_dir, output_name)

    with open(output_path, "wb") as f:
        writer.write(f)

    return output_path


def main():
    print("=== PDF Page Extractor ===\n")

    input_path = prompt_pdf_path()

    reader = PdfReader(input_path)
    total_pages = len(reader.pages)
    print(f"\n  '{os.path.basename(input_path)}' has {total_pages} page(s).")

    print("\nPage range to extract:")
    start_page, end_page = prompt_page_range(total_pages)

    print()
    output_name = prompt_output_name()

    print("\nExtracting pages...")
    output_path = extract_pages(input_path, start_page, end_page, output_name)

    pages_extracted = end_page - start_page + 1
    print(f"\nDone! Extracted {pages_extracted} page(s) to:\n  {output_path}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nAborted.")
        sys.exit(0)
