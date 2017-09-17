# works 100%

Size = [4,3,2,1,5]
Dir = [0,1,0,0,0]

def solution(A, B):
	alive = 0
	stack = []
	for i in range(len(A)):
		if B[i] == 0:
			while len(stack) != 0:
				if stack[-1] > A[i]:
					break
				else:
					stack.pop()
			else:
				alive += 1
		else:
			stack.append(A[i])
	alive += len(stack)
	return alive
	


print(solution(Size, Dir))