def simplifyPath(path: str):
    stack = []
    operations = path.split("/")
    for operation in operations:
        if operation == "..":
            if stack:
                stack.pop()
            continue
        if operation == "." or operation == "/" or operation == "":
            continue
        else:
            stack.append(operation)

    res = "/".join(stack)
    if len(res) == 0 or res[0] != "/":
        res = "/" + res
    return res


print(simplifyPath("/.../a/../b/c/../d/./"))
# print(simplifyPath("/../"))
