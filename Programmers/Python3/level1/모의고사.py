def solution(answers):
    # count_a = 0
    # count_b = 0
    # count_c = 0
    # a = [1, 2, 3, 4, 5]
    # b = [2, 1, 2, 3, 2, 4, 2, 5]
    # c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    # supoja = dict(count_a = 1, count_b = 2, count_c = 3)
    # i = 0
    # for ans in answers:
    #     if a[i % len(a)] == ans:
    #         count_a += 1
    #     if b[i % len(b)] == ans:
    #         count_b += 1
    #     if c[i % len(c)] == ans:
    #         count_c += 1
    #     i += 1
    # if max(count_a, count_b, count_c) == count_a:
    #     if (count_a == count_b):
    #         if count_a == count_c:
    #             return [1, 2, 3]
    #         return [1, 2]
    #     if (count_a == count_c):
    #         return [1, 3]
    #     return[1]
    # elif max(count_a, count_b, count_c) == count_b:
    #     if count_b == count_c:
    #         return [2, 3]
    #     return [2]
    # elif max(count_a, count_b, count_c) == count_c:
    #     return [3]
    result = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    student = [0, 0, 0]
    len1 = len(one)
    len2 = len(two)
    len3 = len(three)
    i = 0
    for a in answers:
        if a == one[i % len1]:
            student[0]+=1
        if a == two[i % len2]:
            student[1]+=1
        if a == three[i % len3]:
            student[2]+=1
        i+=1
    max_num = max(student)
    for i in student:
        if i == max_num:
            max_idx = student.index(i)
            result.append(max_idx+1)
            student[max_idx] = 0
    return result