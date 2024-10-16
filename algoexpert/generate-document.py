def generateDocument(characters, document):
    characters_set = {}
    for letter in characters:
        characters_set[letter] = characters.count(letter)
    for letter in document:
        if letter not in characters_set:
            return False
        if document.count(letter) > characters_set[letter]:
            return False

    return True

print(generateDocument("Bste!hetsi ogEAxpelrt x ", "AlgoExpert is the Best!"))