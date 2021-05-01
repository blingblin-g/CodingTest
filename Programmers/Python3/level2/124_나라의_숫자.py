def to_124(n):
    answer = ''
    while (n):
        answer = str(n % 3) + answer
        print("answer == ", answer)
        n = n // 3
        print("n == ", n)
    result = answer
    print("result == ", result)
    return result

def solution(n):
    answer = jinsu(n)
    print(answer)
    return answer

print(int('12121', 3))

print(to_124(151))

print(to_124(3))