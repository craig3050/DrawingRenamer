import PyPDF2
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
    source = file_path.split("/")[-1]
    file_extension = source.split(".")[-1]
    destination = file_path.replace(source, new_drawing_number + "." + file_extension)
    os.rename(file_path, destination)


def RegExTest(input_text, regex_format):
    output_text = ""
    regex_variable = "."
    for char in regex_format:
        if char == "-":
            output_text += "-"
        else:
            output_text += regex_variable
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


def select_option_1(file_path):
    #Text remove / replace function in filename
    #Use this if lots of the drawing number is the same
    text_remove = input("Enter the text you would like to remove / replace: ")
    text_replace = input("Enter the text you would like to add. Enter nothing for delete only: ")
    for file_name in os.listdir(file_path):
        source = sanitisedFilePath(file_path)
        source += ("/" + file_name)
        if text_remove in file_name:
            destination = file_name.replace(text_remove, text_replace)
            destination = destination.split(".")[0]
            RenameFile(source, destination)


def select_option_2(file_path):
    #add text to the beginning of the filename
    text_add = input("Enter the text you would like to add to the beginning of the file name: ")
    for file_name in os.listdir(file_path):
        source = sanitisedFilePath(file_path)
        source += ("/" + file_name)
        destination = text_add + file_name
        destination = destination.split(".")[0]
        RenameFile(source, destination)


def select_option_3(file_path):
    #add text to the end of the filename
    text_add = input("Enter the text you would like to add to the end of the file name: ")
    for file_name in os.listdir(file_path):
        source = sanitisedFilePath(file_path)
        source += ("/" + file_name)
        destination = file_name.split(".")[0]
        destination = destination + text_add
        RenameFile(source, destination)


def select_option_4(file_path):
    #rename the file based on what is in the titleblock
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




if __name__ == '__main__':
    print("Welcome to Craig's simple file renaming tool!\n\n")
    file_path = input("Enter the Path of the folder to be processed: ")
    print("Printing directory contents: \n")
    for file_name in os.listdir(file_path):
        print(file_name)
        print("\n")

    print (""" \n\n
    What would you like to do: \n
    1. Text Remove / Replace Function
    2. Add Text to Beginning of File Name
    3. Add Text to End of File Name
    4. Rename drawings to whatever is in the PDF titleblock
    """)
    choice = input("Please enter your choice: ")
    if choice == "1":
        select_option_1(file_path)
    elif choice == "2":
        select_option_2(file_path)
    elif choice == "3":
        select_option_3(file_path)
    elif choice == "4":
        select_option_4(file_path)
    else:
        print ("Not a valid choice\nBye bye")

