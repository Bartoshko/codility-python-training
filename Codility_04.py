# works 100%

A = [3,1,2,4,3]
B = [-1,-2,1,0]
C = [-1000,1000]
D = [1000,-1000]

# works for 100%

def solution(A):
	if len(A) <=1:
		return 0
	sum = 0
	arr = []
	for a in A:
		sum = sum + a
		arr.append(sum)
	arr.pop()
	difArr = []
	for i in arr:
		difArr.append(abs((sum - i) - i))
	return min(difArr)
	

print(solution(A))
print(solution(B))
print(solution(C))
print(solution(D))