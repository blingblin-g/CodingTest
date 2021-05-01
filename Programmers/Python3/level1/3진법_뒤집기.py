def jinsu(n):
    answer = ''
    while n:
        answer += str(n % 3)
        n //= 3
    return answer
        
def solution(n):
    return int(jinsu(n), 3)