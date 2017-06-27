import PyPDF2
import argparse

#need pip install pypdf2
#if error with UTF / charmap encoding run the following command in the CMD line - chcp 65001

def extract_pdf_text(file_path):
    with open(file_path, 'rb') as file_open:
        file_object = PyPDF2.PdfFileReader(file_open)
        page_object = file_object.getPage(0)
        page_object = page_object.extractText()

    print(page_object)





if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='Add file path')
    args = parser.parse_args()
    extract_pdf_text(args.path)