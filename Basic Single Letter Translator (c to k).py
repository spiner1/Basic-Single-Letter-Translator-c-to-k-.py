def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "c":
            if letter.isupper():
                translation = translation + "K"
            else:
                translation = translation + "k"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))