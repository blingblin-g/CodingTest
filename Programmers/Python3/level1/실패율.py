import operator

def solution(N, stages):
    answer = dict()
    size = len(stages)
    for i in range(1, N + 1):
        if size == 0:
            answer[i] = 0
        else:
            answer[i] = stages.count(i) / size
            size -= stages.count(i)
    answer = sorted(answer, key = lambda k : answer[k], reverse = True)
    return answer