# works 100%

arr_01 = [8,8,5,7,9,8,7,4,8]

arr_02 = [8,8,5,7,9,8,7,5,8]

arr_03 = [x * 5 for x in range(10000)]
arr_04 = []
arr_04.extend(arr_03)
arr_04.reverse()
arr_05 = arr_03 + arr_04


arr_03 = [1,2]
	
def solution(A):
	count = 0
	stack = []
	for height in A:
		while len(stack) != 0 and stack[-1] > height:
			stack.pop()
		if len(stack) == 0 or stack[-1] != height:
			count += 1
			stack.append(height) 
	return count


print(solution(arr_01))
print('-------------')
print(solution(arr_02))
print('-------------')
print(solution(arr_03))
print('-------------')
print(solution(arr_05))