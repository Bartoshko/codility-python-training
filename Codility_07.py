# works 100%

arr_1 = [1,4,2,3,7,6,5,9,8]
arr_2 = [1,6,9,2,4,5,8,7]
arr_3 = [1,3,4,2]
arr_4 = [1,2,3,1]

def solution(A):
	set_A = set(A)
	if len(set_A) == len(A):
		checker = 1
		for item in set_A:
			if item == checker:
				checker += 1
			else:
				return 0
		return 1
	return 0

print(solution(arr_1))

print(solution(arr_2))

print(solution(arr_3))

print(solution(arr_4))