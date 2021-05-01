def solution(nums):
    case = len(set(nums))
    max_nums = len(nums) // 2
    if max_nums >= case:
        answer = case
    else:
        answer = max_nums
    return answer