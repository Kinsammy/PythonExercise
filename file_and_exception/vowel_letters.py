vowel_input_file = open("word.txt", "r")
vowel_output = open("vowels.txt", "w")
search_word = ''
for word in vowel_input_file:
    for word_str in word:
        if word_str in ['a', 'e', 'i', 'o', 'u']:
            search_word += word_str
    if search_word == 'aeiou':
        print(word, end=' ')
    print(search_word, file=vowel_output)

    search_word = ''
vowel_input_file.close()
vowel_output.close()