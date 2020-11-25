# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

with open("ciphertext.txt") as f:
    ciphered_text_string = f.read()

# just keeping these variables global for now
total_letters = 0
letter_count_dictionary = { }
letter_count_percentage_dictionary = { }
letters = []
deciphered_text = ""
decoded_letters = {}

def letter_count():
    global total_letters

    for letter in ciphered_text_string:
        if letter >= "A" and letter <= "Z":
            total_letters += 1
            if letter not in letter_count_dictionary:
                letter_count_dictionary[letter] = 0
            else:
                letter_count_dictionary[letter] += 1
                
def letters_frequency():
    global letters
    global letter_count_percentage_dictionary
    letters = list(letter_count_dictionary.keys())
    for letter in letters:
        letter_count_percentage_dictionary[letter] = float(letter_count_dictionary[letter]) / float(total_letters) * 100
    letters.sort(key = lambda letter: letter_count_dictionary[letter], reverse = True)
    
def decrypt_letters():
    global decoded_letters

    letters_by_use_frequency = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
    i = 0
    while i < len(letters):
        decoded_letters[letters[i]] = letters_by_use_frequency[i]
        i += 1

def decrypt_ciphered_text():
    global deciphered_text

    i = 0
    while i < len(ciphered_text_string):
        if ciphered_text_string[i] >= "A" and ciphered_text_string[i] <= "Z":
            deciphered_text += decoded_letters[ciphered_text_string[i]]
        else:
            deciphered_text += ciphered_text_string[i]
        i += 1

def decipher_text():
    # read the cipheredText file
    with open("ciphertext.txt") as f:
        ciphered_text_string = f.read()
    # get count of all letters and each letter's count
    letter_count()
    # get list of letters aranged by their frequency (to make sure they line up with letter use frquency)
    letters_frequency()
    # get dictionary of letters mapped to their decrypted letter
    decrypt_letters()
    # decrypt ciphered text
    decrypt_ciphered_text()
    # print deciphered text
    print(deciphered_text)

decipher_text()
