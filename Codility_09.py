# 100%
arr_01 = [3,4,4,6,1,4,4]
n = 5

def solution(n, arr):
    out = [0] * n
    m = 0
    last = 0
    for op in arr:
        op -= 1
        if op == n:
            last = m
            continue
        out[op] = max(out[op], last) + 1
        m = max(m, out[op])
    for i in range(n):
        out[i] = max(out[i], last)

    return out

print(solution(n, arr_01))
