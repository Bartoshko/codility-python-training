#  works 100%

A = []

def solution(A, K):
	if len(A) == 0:
		return A
	M = K
	if K > len(A):
		M = K % len(A)
	return A[len(A)-M:len(A)] + A[0:len(A)-M]

print(solution(A, 42))