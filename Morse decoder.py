MORSE_CODE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}

def morse_decode(morse_code):
    # Check if input is valid Morse code
    valid_morse_chars = set(".- ")
    if any(c not in valid_morse_chars for c in morse_code):
        return "Invalid Morse code input"
    
    words = morse_code.split("  ")
    decoded_words = []
    for word in words:
        letters = word.split()
        decoded_letters = []
        for letter in letters:
            decoded_letters.append(MORSE_CODE[letter])
        decoded_word = "".join(decoded_letters)
        decoded_words.append(decoded_word)
    decoded_sentence = " ".join(decoded_words)
    return decoded_sentence.capitalize().rstrip()

#Here's a Python program that decodes a Morse code string using the given MORSE_CODE dictionary, capitalizes the first letter of each sentence, and removes the trailing whitespace:

python
Copy code
MORSE_CODE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}

def morse_decode(morse_code):
    words = morse_code.split("  ")
    decoded_words = []
    for word in words:
        letters = word.split()
        decoded_letters = []
        for letter in letters:
            decoded_letters.append(MORSE_CODE[letter])
        decoded_word = "".join(decoded_letters)
        decoded_words.append(decoded_word)
    decoded_sentence = " ".join(decoded_words)
    return decoded_sentence.capitalize().rstrip()

# The morse_decode function first splits the Morse code string into words using double spaces as the delimiter. 
# It then splits each word into letters using single spaces as the delimiter, and decodes each letter using the MORSE_CODE dictionary. 
# It then joins the decoded letters to form the decoded word, and appends it to a list of decoded words. 
# Finally, it joins the decoded words to form the decoded sentence, capitalizes the first letter of the sentence using the capitalize method, and removes the trailing whitespace using the rstrip method.
