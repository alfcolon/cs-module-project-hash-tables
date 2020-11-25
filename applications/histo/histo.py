# Read in all the words in one go
with open("robin.txt") as f:
    string = f.read()

word_count_dictionary = {}

def word_count():
    global string
    global word_count_dictionary
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
            if word in word_count_dictionary:
                word_count_dictionary[word] += 1
            else:
                word_count_dictionary[word] = 1
            word = ""
        i += 1
    return word_count_dictionary

def histogram():
    # populate word_count_dictionary
    word_count()
    # sort keys alphabetically and then their value in decending order
    word_count_dictionary_keys = list(word_count_dictionary.keys())
    word_count_dictionary_keys.sort()
    word_count_dictionary_keys.sort(key = lambda str: word_count_dictionary[str], reverse = True)
    # create longest histogram value for output
    histogram_value = "#" * word_count_dictionary[word_count_dictionary_keys[0]]
    # iterate through the keys and print out the word and it's histogram value
    for word in word_count_dictionary_keys:
        length = word_count_dictionary[word]
        # just using a random width for word and histogram
        print(f'{word:20} {histogram_value[:length]:30}')
        
histogram()
