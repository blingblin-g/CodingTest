def solution(array, commands):
    answer = []
    arr = list(array)
    for i in range(len(commands)):
        haha = arr[commands[i][0] - 1:commands[i][1]]
        haha.sort()
        answer.append(haha[commands[i][2] - 1])
    return answer