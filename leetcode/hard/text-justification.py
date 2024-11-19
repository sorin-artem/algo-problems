def fullJustify(words, maxWidth):
    line = []
    length = 0
    res = []
    for i in range(len(words)):
        if len(words[i]) + length + len(line) > maxWidth:
            left_space = maxWidth - length
            extra_spaces = left_space // max(len(line) - 1, 1)
            remainder = left_space % max(len(line) - 1, 1)

            for j in range(max(len(line) - 1, 1)):
                line[j] += " " * extra_spaces
                if remainder:
                    line[j] += " "
                    remainder -= 1

            res.append("".join(line))

            line =[]
            length = 0
        line.append(words[i])
        length += len(words[i])

    last_line = " ".join(line)
    extra_spaces = maxWidth - len(last_line)
    res.append(last_line + " "*extra_spaces)
    return res
