# works 77%
from functools import reduce
arr_1 = [1,3,6,4,1,2]
arr_2 = [-1,-3]
arr_3 = [1,2,3]
arr_4 = [2,3,4]
arr_5 = [-1,-2,1,2,3]
arr_6 = [-100000,1,2,3,4,5,6,7,8,9,10,11]

def solution(A):
	set_A = set()
	for item in A:
		if item > 0:
			set_A.add(item)
	set_B = set(list(map(lambda x: x+1, range(len(set_A)+1))))
	return set_B.difference(set_A).pop()

print(solution(arr_1))

print(solution(arr_2))

print(solution(arr_3))

print(solution(arr_4))

print(solution(arr_5))

print(solution(arr_6))