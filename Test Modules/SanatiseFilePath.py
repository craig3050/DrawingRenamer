
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
    file_path = input("Enter the Path Directory: ")
    print (sanitisedFilePath(file_path))


