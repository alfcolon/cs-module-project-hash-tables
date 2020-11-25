
def word_count(string):
    word_dictionary = {}
    encoded_string = string.encode()
    stringLen = len(string)
    
    word = ''
    i = 0
    while i < stringLen:
        
        character_ascii_value = encoded_string[i]
        if character_ascii_value >= 65 and character_ascii_value <= 90:
            word += string[i].lower()
        elif character_ascii_value >= 97 and character_ascii_value <= 122:
            word += string[i]
        elif character_ascii_value == 39:
            word += string[i]
        elif word != "":
            if word in word_dictionary:
                word_dictionary[word] += 1
            else:
                word_dictionary[word] = 1
            word = ""
        i += 1
    return word_dictionary


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
