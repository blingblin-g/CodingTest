import math

def solution(progresses, speeds):
    schedule = []
    answer = []
    result = []
    count = 0
    for i, item in enumerate(progresses):
        task = 100 - progresses[i]
        time = math.ceil(task / speeds[i])
        schedule.append(time)
    
    print(schedule)
    max_t = schedule[0]
    for i, t in enumerate(schedule):
        if max_t >= t:
            count += 1
        else:
            max_t = t
            answer.append(t)
            result.append(count)
            count = 1
    result.append(count)
    return result

print(solution([93, 30, 55], [1, 30, 5]))
