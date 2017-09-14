# works 100%

arr_0 = [0,1,0,1,1]
arr_1 = [0,1,0,1,0,1,0,1,0,1]

def solution(A):
	increment = 0
	counter = 0
	value = 0
	for i in A:
		if i == 0:
			increment += 1
		if i == 1:
			value += increment
			counter += increment
		if counter > 1000000000:
			return -1
	return counter

print(solution(arr_0))

print(solution(arr_1))