works 100%

arr_1 = [10, 2, 5, 1 ,8, 20]
arr_2 = [10, 50, 5, 1]

def solution(A):
    A = sorted(A)
    a = b = c = 0
    for i in reversed(A):
        a, b, c = i, a, b
        if a + b > c and a + c > b and c + b > a:
            return 1
    else:
        return 0


print(solution(arr_1))

print(solution(arr_2))