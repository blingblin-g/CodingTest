def solution(numbers):
    answer = []
    for num, i in enumerate(numbers):
        for idx, j in enumerate(numbers):
            if num != idx and i + j not in answer:
                answer.append(i+j)
    
    answer.sort()
    return answer