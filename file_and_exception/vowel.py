if __name__ == '__main__':
    temp_file = open("vowel_sound", "w")
    words = "facetious"
    vowels = 0
    for index in words:
        if index == 'a' or index == 'e' or index == 'i' or index == 'o' or index == 'u':
            vowels += 1
            print(index, file=temp_file)
    print(vowels)
    temp_file.close()
