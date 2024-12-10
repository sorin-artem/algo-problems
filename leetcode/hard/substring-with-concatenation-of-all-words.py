from copy import deepcopy


def findSubstring(s, words):
    freq_map = {}
    current_map = {}
    res = []

    for word in words:
        if word in freq_map:
            freq_map[word] += 1
        else:
            freq_map[word] = 1
    print(freq_map)

    word_size = len(words[0])
    window_size = word_size * len(words)
    for i in range(0, len(words[0]), 1):
        start = i
        while start + window_size - 1 < len(s):
            current_map = deepcopy(freq_map)
            matched = True
            for j in range(len(words)):
                current_word = s[start + j * word_size:start + j * word_size + word_size]
                if current_word not in current_map or current_map[current_word] == 0:
                    matched = False
                    break
                current_map[current_word] -= 1
            if matched:
                res.append(start)
            start += word_size
    return res
print(findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
