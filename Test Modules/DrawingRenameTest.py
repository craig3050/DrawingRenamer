import os

def RenameFile(file_path, new_drawing_number):
    source = file_path.split("/")[-1]
    file_extension = source.split(".")[-1]
    print (source)
    print (file_extension)
    destination = file_path.replace(source, new_drawing_number + "." + file_extension)
    print (destination)
    os.rename(file_path, destination)

if __name__ == '__main__':
    file_path = input("Enter the Path Directory: ")
    new_number = "EGIP19-abc-def-eft-22-345"
    RenameFile(file_path, new_number)

