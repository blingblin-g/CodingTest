def solution(seoul):
    for num, i in enumerate(seoul):
        if i == "Kim":
            answer = "김서방은 " + str(num) + "에 있다"
    return answer