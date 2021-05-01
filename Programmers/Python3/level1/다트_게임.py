def solution(dartResult):
    i = 0
    score = ['', '', '']
    bonus = ['', '', '']
    option = ['', '', '']
    for part in dartResult:
        if part.isdigit():
            if bonus[i]:
                i += 1
            score[i] += part
        elif part in ['*', '#']:
            option[i] = part
            i += 1
        elif part in ['S', 'D', 'T']:
            bonus[i] += part
    idx = 0
    score = list(map(int, score))
    prev_score = 0
    answer = [0, 0, 0]
    for s, b in zip(score, bonus):
        if b == 'S':
            answer[idx] = s ** 1
        elif b == 'D':
            answer[idx] = s ** 2
        elif b == 'T':
            answer[idx] = s ** 3
        if option[idx] == '*':
            answer[idx] = answer[idx] * 2
            if idx != 0:
                answer[idx - 1] = answer[idx - 1] * 2
        elif option[idx] == '#':
            answer[idx] = answer[idx] * (-1)

        idx += 1
        prev_score = s
    answer = sum(answer)
    return answer