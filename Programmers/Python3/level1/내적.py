def solution(a, b):
    answer = 0
    for p1, p2 in zip(a,b):
        answer += p1 * p2
    return answer