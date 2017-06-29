import os
import openpyxl
from openpyxl import Workbook

def excel_list(file_path):
    drawing_list = Workbook()
    worksheet_1 = drawing_list.active
    drawing_list.save("Drawing_list.xlsx")
    row_number = 1
    for file_name in os.listdir(file_path):
        worksheet_1.cell(row = row_number, column = 1).value = file_name
        row_number += 1
    drawing_list.save("Drawing_list.xlsx")











if __name__ == '__main__':
    print("Welcome to Craig's simple file renaming tool!\n\n")
    file_path = input("Enter the Path of the file to be processed: ")
    excel_list(file_path)
    temp_var = input("Press enter once you have added the destination drawing numbers")
