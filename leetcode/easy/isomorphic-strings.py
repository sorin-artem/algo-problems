def isIsomorphic(s, t):
    s_hash = {}
    t_hash = {}
    for i in range(len(s)):
        c1, c2 = s[i], t[i]

        if c1 in s_hash:
            if s_hash[c1] != c2:
                return False
        if c2 in t_hash:
            if t_hash[c2] != c1:
                return False
        s_hash[c1] = c2
        t_hash[c2] = c1

    return True



print(isIsomorphic("fos", "baa"))