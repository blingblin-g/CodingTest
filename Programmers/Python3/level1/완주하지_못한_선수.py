def solution(participant, completion):
    runners = {}
    for i in participant:
        try: runners[i] += 1
        except: runners[i] = 1
    for i in completion:
        runners[i] -= 1
        if runners[i] == 0:
            del runners[i]
    return ''.join(runners.keys())