def solution(p: str) -> str:
    LEFT = "("
    RIGHT = ")"

    def is_balanced(s: str) -> bool:
        left = right = 0
        for char in s:
            if char == LEFT:
                left += 1
            else:
                right += 1
        return left == right

    def is_right(s: str) -> bool:
        if not is_balanced(s):
            return False

        stack = []
        for char in s:
            if char == LEFT:
                stack.append(char)
            else:
                if not stack:
                    return False
                stack.pop()
        if stack:
            return False
        return True

    # 인덱스 처리 어려움
    def _solution(part: str) -> str:
        if part == "":
            return ""
        u = ""
        v = ""
        # 길이가 2일때 처리 안됨
        # for index in range(2, len(part), 2):
        #     u += part[index - 2:index]
        #     if is_balanced(u):
        #         v = part[index:]
        #         break

        for index in range(1, len(part), 2):
            u += part[index - 1:index + 1]
            if is_balanced(u):
                v = part[index + 1:]
                break

        if is_right(u):
            return u + _solution(v)
        else:
            return "(" + _solution(v) + ")" + ''.join(RIGHT if x == LEFT else LEFT for x in u[1:-1])

    return _solution(p)


print(solution("(()())()"))
