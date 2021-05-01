def solution(n, m):
    answer = []
    for i in range(2, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            answer = [i]
    if answer == []:
        answer.append(1)
        answer.append(n * m)
    else:
        n = n // answer[0]
        m = m // answer[0]
        answer.append(n * m * answer[0])
    return answer