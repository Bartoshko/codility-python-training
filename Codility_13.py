works 100%

arr_1 = [-3,1,2,-2,5,6]

def solution(A):
	A = sorted(A)
	max_triplet_rigt = A[len(A)-3]*A[len(A)-2]*A[len(A)-1]
	max_triplet_left = A[0]*A[1]*A[len(A)-1]
	if max_triplet_rigt > max_triplet_left:
		return max_triplet_rigt
	else:
		return max_triplet_left
	

print(solution(arr_1))