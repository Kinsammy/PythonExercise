def main():
    # open file for output
    outfile = open("presidents.txt", "w")
    outfile.write("Samuel Fanu Ibukun\n")
    outfile.write("Bill Clinton\n")
    outfile.write("George Bush\n")
    outfile.write("Barack Obama")
    outfile.close()


if __name__ == '__main__':
    main()
