# works for 100%

from functools import reduce
A = [2,3,1,5]
B = []
C = [1]
D = [2]

def solution(A):
	if len(A) == 0:
		return 1
	sum = reduce(lambda x,y: x+y, A)
	fullSum = 0
	for i in range(len(A)+2):
		fullSum = fullSum + i
	return fullSum - sum

print(solution(A))

print(solution(B))

print(solution(C))

print(solution(D))