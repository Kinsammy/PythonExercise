if __name__ == '__main__':

    temp_file = open("../file_and_exception/temp.text", "w")
    print("first line", file=temp_file)
    print("second line", file=temp_file)
    temp_file.close()
