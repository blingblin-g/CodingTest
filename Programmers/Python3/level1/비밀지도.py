def process(brr, n):
    return (n - len(brr[2:])) * '0' + brr[2:]
def solution(n, arr1, arr2):
    answer = ["" for i in range(n)]
    brr1 = [process(bin(i), n) for i in arr1]
    brr2 = [process(bin(i), n) for i in arr2]
    for i in range(n):
        for j in range(len(brr1)):
            if brr1[i][j] == '1' or brr2[i][j] == '1':
                answer[i] += '#'
            else:
                answer[i] += ' '
    return answer