# works 100%

def solution(X, Y, D):
	if (Y - X) % D == 0:
		return int(round(Y - X) / D)
	return int(round((Y - X) / D) + 1)



print(solution(10, 85, 30))
print(solution(101, 850, 30))
print(solution(1, 8, 1))
print(solution(2, 14, 2))
