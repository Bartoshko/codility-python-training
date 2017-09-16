# works 100%

arr_01 = [1,5,2,1,4,0]

def solution(A):
    endpoints = []
    for i, a in enumerate(A):
        endpoints += [(i-a, True), (i+a, False)]

    endpoints.sort(key=lambda x: (x[0], not x[1]))
    counter, active = 0, 0
 
    for _, beginning in endpoints:
        if beginning:
            counter += active
            active += 1
        else:
            active -= 1
        if counter > 10E6:
            return -1
    return counter

print(solution(arr_01))

