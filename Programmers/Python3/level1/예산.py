def solution(d, budget):
    count = 0
    init_d = len(d)
    while(sum(d) > budget):
        d.remove(max(d))
        count += 1
    answer = init_d - count
    return answer