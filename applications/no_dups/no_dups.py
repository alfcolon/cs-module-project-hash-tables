def no_dups(string):
    unique_words_string = ''
    word = ""
    word_dictionary = { }
    
    string_len = len(string)
    encoded_string = string.encode()
    
    i = 0
    while i < string_len:
        character_ascii_value = encoded_string[i]
        # letters
        if (character_ascii_value >= 65 and character_ascii_value <= 90) or (character_ascii_value >= 97 and character_ascii_value <= 122):
            word += string[i]
        # ' character
        elif character_ascii_value == 32:
            if word != "":
                if word not in word_dictionary:
                    if unique_words_string != "":
                        unique_words_string += ' '
                    unique_words_string += word
                    word_dictionary[word] = 1
                word = ""
        i += 1
    if unique_words_string == "" and word != "":
        return word
    return unique_words_string

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
