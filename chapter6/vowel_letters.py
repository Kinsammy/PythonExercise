if __name__ == '__main__':
    words = "facetious"
    vowels = 0

    for index in words:
        if index == 'a' or index == 'e' or index == 'i' or index == 'o' or index == 'u':
            vowels += 1
            print("vowels is: %s" % index)
    print(vowels)
