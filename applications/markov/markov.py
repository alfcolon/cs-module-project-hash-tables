import random

# Read in all the words in one go
with open("input2.txt") as f:
    words = f.read()

def is_starting_word(word):
    first_character = word[0]
    return first_character.isupper() or first_character == '"'

def is_stopping_word(word):
    last_character = word[-1]
    return last_character == "." or last_character == "?" or last_character == "!" or last_character == '"'
    
# TODO: analyze which words can follow other words
split_words = words.split()

word_bank = {
    "unique starting words": [],
    "unique stopping words": [],
    "unique stopping words with quotes": [],
    "words with next words": {}
}

# TODO: analyze which words can follow other words
def build_word_bank():
    word_count = len(split_words)
    i = 0
    while i < word_count:
        word = split_words[i]
        if word not in word_bank["words with next words"]:
            if is_starting_word(word):
                word_bank["unique starting words"].append(word)
            if is_stopping_word(word):
                if word[-1] == '"':
                    word_bank["unique stopping words with quotes"].append(word)
                else:
                    word_bank["unique stopping words"].append(word)
            word_bank["words with next words"][word] = []
        if i < word_count - 1:
            nextWord = split_words[i + 1]
            word_bank["words with next words"][word].append(nextWord)
        i += 1

# TODO: construct 5 random sentences
build_word_bank()

for i in range(5):
    print(f"Sentence #{i + 1}:")
    word = random.choice(word_bank["unique starting words"])
    if word[-1] == "t":
        print(True)
    started_with_quotes = word[0] == '"' or word[-1] == '"'
    print(word, end = " ")
    while True:
        word = random.choice(word_bank["words with next words"][word])
        if is_stopping_word(word):
            if started_with_quotes:
                if word[-1] != '"':
                    word = random.choice(word_bank["unique stopping words with quotes"])
            print(word)
            break
        print(word, end = " ")
    print("\n")
