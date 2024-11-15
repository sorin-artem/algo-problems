def reverse(s):
    res = ""

    i = len(s) - 1
    word = ""
    while i >= 0:
        if s[i] == " ":
            i -= 1
            continue
        word = s[i] + word
        if i == 0 or s[i - 1] == " ":
            res += word + " "
            word = ""
        i -= 1

    if res[len(res) - 1] == " ":
        return res[:len(res) - 1]

    return res

print(reverse("a good   example"))