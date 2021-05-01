from itertools import combinations
import math

def is_prime_number(num):
    if num < 2:
        return False
    else:
        root_num = int(math.sqrt(num))
        for n in range(2, root_num + 1):
            if num % n == 0:
                return False
        return True

def solution(nums):
    answer = 0
    cmb = list(combinations(nums,3))
    sum_cmb = []
    for i in cmb:
        sum_cmb.append(sum(i))
    for arr in sum_cmb:
        if is_prime_number(arr):
            answer += 1
    return answer