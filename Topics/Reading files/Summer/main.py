#  write your code here 
def read_lines(filename:str)->list:
    text_file = open(filename, "r")
    with text_file:
        file_content = text_file.readlines()
    text_file.close()
    return file_content


if __name__ == "__main__":
    content = read_lines("hyperskill-dataset-84596997.txt")
    print(content)
    print(content.count("summer\n"))
