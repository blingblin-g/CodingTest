def solution(s):
    answer = ""
    s = list(s)
    n = 0
    for i in range(len(s)):
        if s[i] == ' ':
            n = 0
            continue
        if n == 0:
            s[i] = s[i].upper()
            n = 1
            continue
        if n == 1:
            s[i] = s[i].lower()
            n = 0
            continue
        # if s[i] != '':
        #     for p in range(len(s[i])):
        #         if p % 2 == 0:
        #             s[i][p] = s[i][p].upper()
        #         elif p % 2 == 1:
        #             print("1: ", s[i][p])
        #             s[i][p] = s[i][p].lower()
        
        # if s[i] == '':
        #     space = 0
        #     continue
        # elif space % 2 == 0:
        #     s[i] = s[i].upper()
        # elif space % 2:
        #     s[i] = s[i].lower()
        # space += 1
    answer = (''.join(s))
    return answer