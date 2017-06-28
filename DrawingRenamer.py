import PyPDF2
import argparse
import re
import os

#need pip install pypdf2
#if error with UTF / charmap encoding run the following command in the CMD line - chcp 65001

def extract_pdf_text(file_path):
    with open(file_path, 'rb') as file_open:
        file_object = PyPDF2.PdfFileReader(file_open)
        page_object = file_object.getPage(0)
        page_object = page_object.extractText()

    return page_object


def RenameFile(file_path, new_drawing_number):
    sanitised_file_path = ""
    for char in file_path:
        if char == "\"":
            sanitised_file_path += ""
        elif char == "\\":
            sanitised_file_path += "/"
        else:
            sanitised_file_path += char

    print (sanitised_file_path)

    source = sanitised_file_path.split("/")[-1]
    file_extension = source.split(".")[-1]
    print (source)
    print (file_extension)

    destination = sanitised_file_path.replace(source, new_drawing_number + "." + file_extension)
    print (destination)
    os.rename(sanitised_file_path, destination)


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
    regex_results = re.findall(output_text, input_text)
    print(regex_results)
    number_of_regex_groups = len(regex_results) -1
    return regex_results[number_of_regex_groups]

def sanitisedFilePath(file_path):
    sanitised_file_path = ""

    for char in file_path:
        if char == "\"":
            sanitised_file_path += ""
        elif char == "\\":
            sanitised_file_path += "/"
        else:
            sanitised_file_path += char

    return sanitised_file_path


if __name__ == '__main__':
    print("Welcome to Craig's simple file renaming tool!\n\n")
    file_path = input("Enter the Path of the folder to be processed: ")
    print("Printing directory contents: \n")
    regex_template = input("Enter a sample drawing number: ")
    for file_name in os.listdir(file_path):
        print(file_name)
        print("\n\n\n")
        sanitised_file_path = sanitisedFilePath(file_path)
        sanitised_file_path += "/" + file_name
        pdf_text = extract_pdf_text(sanitised_file_path)
        print (pdf_text)
        pdf_text_match = RegExTest(pdf_text, regex_template)
        RenameFile(sanitised_file_path, pdf_text_match)

