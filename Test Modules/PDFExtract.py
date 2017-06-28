import PyPDF2
import os


#need pip install pypdf2
#if error with UTF / charmap encoding run the following command in the CMD line - chcp 65001

def extract_pdf_text(file_path):
    print (file_path)
    with open(file_path, 'rb') as file_open:
        file_object = PyPDF2.PdfFileReader(file_open)
        page_object = file_object.getPage(0)
        page_object = page_object.extractText()

    return page_object





if __name__ == '__main__':
    print("Welcome to Craig's simple file renaming tool!\n\n")
    file_path = input("Enter the Path of the file to be processed: ")
    print (extract_pdf_text(file_path))

