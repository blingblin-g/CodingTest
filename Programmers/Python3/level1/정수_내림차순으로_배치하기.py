def solution(n):
    a = []
    answer = 0
    for i in range(len(str(n))):
        a.append(n % 10)
        n = n // 10
    a.sort()
    while (i > -1):
        answer = answer * 10 + int(a[i])
        i -= 1
    return answer