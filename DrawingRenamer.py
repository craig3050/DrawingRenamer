import PyPDF2
import argparse
import re
import shutil
import os

#need pip install pypdf2
#if error with UTF / charmap encoding run the following command in the CMD line - chcp 65001

def extract_pdf_text(file_path):
    with open(file_path, 'rb') as file_open:
        file_object = PyPDF2.PdfFileReader(file_open)
        page_object = file_object.getPage(0)
        page_object = page_object.extractText()

    return page_object


def RegExTest(input_text, regex_format):
    output_text = ""
    regex_variable = "."
    for char in regex_format:
        if char == "-":
            output_text += "-"
        else:
            output_text += regex_variable
    output_text += ""
    print (output_text)
    return re.search(output_text, input_text)

def RenameFile(file_path, drawing_number):

    for file_name in file_path:
        source = file_path.split("/")[-1]
        length = len(file_name)
        #source = file_path + "\\" + file_name
        source = os.path.join(file_path, file_name)
        extension_length = 0
        for x in file_name:
            if x == ".":
                break
            else:
                extension_length += 1
        extension_length =  length - extension_length
        file_name_no_ext = file_name[0:length - extension_length] #removes the extension
        destination = os.path.join(file_path, file_name_no_ext + " " + text_input + file_name[-extension_length:]) #-4 is the extension

    destination = file_path + "/processed"
    shutil.copy(file_path, destination)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='Add file path')
    args = parser.parse_args()
    drawing_no = input("Enter Sample Drawing Number: ")
    pdf_text = extract_pdf_text(args.path)
    print (pdf_text)
    pdf_text_match = RegExTest(pdf_text, drawing_no)
    drawing_name = pdf_text_match.group(0)
    RenameFile(args.path, drawing_name)

