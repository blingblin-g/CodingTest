def solution(s):
    len_s = len(s)
    idx = len_s // 2
    return s[idx] if len_s % 2 == 1 else s[idx - 1] + s[idx]