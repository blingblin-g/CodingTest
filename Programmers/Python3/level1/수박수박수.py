def solution(n):
    watermelon = []
    for i in range(n):
        if i % 2 == 0:
            watermelon.append("수")
        if i % 2 == 1:
            watermelon.append("박")
    answer = ''.join(watermelon)
    return answer