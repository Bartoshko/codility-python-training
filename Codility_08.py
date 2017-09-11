# works 100%

arr_1 = [1,3,1,4,2,3,5,4]
arr_2 = [1,1,1,1,2,3,6,8,7,9,3,5,2,8,0,7,4,6,4,9]

def solution(X, A):
	set_A = set()
	time = -1
	for item in A:
		if item <= X:
			set_A.add(item)
		time += 1
		if len(set_A) == X:
			return time
	return -1

print(solution(5, arr_1))

print(solution(5, arr_2))