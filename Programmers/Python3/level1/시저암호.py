def solution(s, n):
    small = "abcdefghijklmnopqrstuvwxyz"
    big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    answer = []
    for i in range(len(s)):
        for j in range(26):
            if s[i] == small[j]:
                a = j + n
                if a >= 26:
                    a= a - 26
                answer.append(small[a])
                break
            if s[i] == big[j]:
                a = j + n
                if a >= 26:
                    a = a - 26
                answer.append(big[a])
                break
        else:
            answer.append(s[i])
            continue
    answer = ''.join(answer)
    return answer