def solution(n, lost, reserve):
    # for i in reserve:
    #     if i in lost:
    #         reserve.remove(i)
    #         lost.remove(i)
    # for i in reserve:
    #     if i - 1 in lost:
    #         lost.remove(i - 1)
    #     elif i + 1 in lost:
    #         lost.remove(i + 1)
    # return n - len(lost)
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    for i in reserve_set:
        if i - 1 in lost_set:
            lost_set.remove(i - 1)
        elif i + 1 in lost_set:
            lost_set.remove(i + 1)
    return n - len(lost_set)