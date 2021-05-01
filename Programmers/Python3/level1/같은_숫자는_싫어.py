def solution(arr):
    # answer = [arr[0]]
    # a = 0
    # for i in range(1, len(arr)):
    #     if arr[i - 1] == arr[i]:
    #         a = 1
    #     else:
    #         a = 0
    #     if a == 0:
    #         answer.append(arr[i])
    # return answer
    a = None
    answer = []
    for i in arr:
        if i != a:
            answer.append(i)
        a = i
    return answer