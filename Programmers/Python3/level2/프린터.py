def solution(priorities, location):
    answer = 0
    len_priorities = len(priorities)
    idx_list = list(range(len_priorities))
    q_list = []
    while True:
        if priorities[0] < max(priorities):
            priorities.append(priorities[0])
            priorities = priorities[1:]
            print(priorities)
            idx_list.append(idx_list[0])
            idx_list = idx_list[1:]
            print(idx_list)
            print("========================================")
        else:
            priorities.pop(0)
            q_list.append(idx_list.pop(0))
            print("priorities", priorities)
            print("q_list", q_list)
        if len(q_list) == len_priorities:
            break
    answer = q_list.index(location) + 1
    return answer

print(solution([1,1,6,2,3,2], 3))
print("========================================")
print("========================================")
print(solution([1, 1, 9, 1, 1, 1], 0))