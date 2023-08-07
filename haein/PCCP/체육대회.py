from itertools import permutations

def solution(ability):
    answer = 0
    arr = list(permutations(ability, len(ability[0])))

    for i in range(len(arr)):
        total = 0
        for j in range(len(ability[0])):
            total += arr[i][j][j]
        answer = max(answer, total)

    return answer
