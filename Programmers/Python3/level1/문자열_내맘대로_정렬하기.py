def solution(strings, n):
    string = sorted(strings, key = lambda e : (e[n], e))
    return string