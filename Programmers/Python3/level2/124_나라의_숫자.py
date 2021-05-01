def solution(n):
    numbers = ['4', '1', '2']
    answer = ''
    while n:
        answer = numbers[n % 3] + answer
        if n % 3 == 0:
            n = n // 3 - 1
        else:
            n //= 3
    return answer