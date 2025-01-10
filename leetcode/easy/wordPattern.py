def wordPattern(pattern, s):
    words = s.split(" ")
    pattern_hash = {}
    words_hash = {}

    if len(words) != len(pattern):
        return False

    for i in range(len(pattern)):
        letter = pattern[i]
        word = words[i]

        if letter in pattern_hash:
            if pattern_hash[letter] != word:
                return False
        if word in words_hash:
            if words_hash[word] != letter:
                return False

        pattern_hash[letter] = word
        words_hash[word] = letter

    return True


print(wordPattern("abba", "dog dog dog dog"))