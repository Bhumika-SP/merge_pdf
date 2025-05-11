import os
from PyPDF2 import PdfMerger

def merge_pdfs(input_paths, output_path):
    try:
        merger = PdfMerger()
        for pdf in input_paths:
            merger.append(pdf)
        merger.write(output_path)
        merger.close()
        print(f"PDFs successfully merged and saved as {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    num_files = int(input("Enter the number of PDF files to merge: "))
    pdf_paths = [input(f"Enter path for PDF {i+1}: ") for i in range(num_files)]
    output_path = input("Enter the output path for the merged PDF: ")
    merge_pdfs(pdf_paths, output_path)
