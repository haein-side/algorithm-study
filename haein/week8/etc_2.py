def solution(S):
    answer = ''
    pair = {"{": "}", "(":")", "[":"]"}

    stack = []

    for char in S:
        if char in pair.keys():
            stack.append(char)
        else:
            if (stack):
                top = stack.pop()
                if (pair[char] != top):
                    return "FALSE"
            else:
                return "FALSE"

    return "TRUE"
