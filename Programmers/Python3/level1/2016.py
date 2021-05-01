def solution(a, b):
    arr = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    result = 0
    for i in range(a - 1):
        result += arr[i]
    result += b
    result = result % 7
    answer = week[result]
    return answer