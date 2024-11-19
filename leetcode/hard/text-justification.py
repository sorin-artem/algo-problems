def fullJustify(words, maxWidth):
    res = []
    line = []
    length = 0

    i = 0
    while i < len(words):
        # len(line) means amount of single spaces (" ") because at least one space is required
        if length + len(line) + len(words[i]) > maxWidth:
            extra_spaces = maxWidth - length

            # avoid division by 0
            spaces = extra_spaces // max(1, len(line) - 1)
            remainder = extra_spaces % max(1, len(line) - 1)

            # -1 avoid space for last word, max to have at least one iteration
            for j in range(max(1, len(line) - 1)):
                line[j] += " " * spaces
                if remainder != 0:
                    line[j] += " "
                    remainder -= 1

            res.append("".join(line))
            line = []
            length = 0

        line.append(words[i])
        length += len(words[i])
        i += 1
    last_line = " ".join(line)
    extra_spaces = len(maxWidth) - len(last_line)
    res.append(last_line + " " * extra_spaces)

    return res
