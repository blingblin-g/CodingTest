def solution(arr, divisor):
    # answer = [i for i in arr if i % divisor == 0]
    # if answer == []:
    #     return [-1]
    # return sorted(answer)
    answer = [i for i in arr if i % divisor == 0]
    return [-1] if answer == [] else sorted(answer)