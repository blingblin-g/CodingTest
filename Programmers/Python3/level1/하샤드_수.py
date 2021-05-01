def solution(x):
    n = str(x)
    sam = 0
    for i in range(len(n)):
        sam += int(n[i])
    if x % sam == 0:
        return(True)
    else:
        return(False)