newVowelLibrary = {
    "a": "g",
    "e": "b",
    "i": "r",
    "o": "t",
    "u": "l"
}


def translate(phrase, vowel_library):
    translation = ""

    for letter in phrase:
        if letter.lower() in vowel_library:
            translation += vowel_library[letter]
        else:
            translation += letter

    return translation.lower()


while True:
    print(translate(input("Input a phrase to translate:\n"), newVowelLibrary))
