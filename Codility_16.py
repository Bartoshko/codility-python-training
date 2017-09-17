# works 100%

string_1 = '{[()()]}'
string_2 =  '([)()]'
string_3 = '(()(((())(()))))'

def Paired(left, right):
	if left == '(' and right == ')':
		return True
	if left == '[' and right == ']':
		return True 
	if left == '{' and right == '}':
		return True   
	return False
def solution(S):
	stack = []
	for symbol in S:
		if symbol == '[' or symbol == '{' or symbol == '(':
			stack.append(symbol)
		else:
			if len(stack) == 0:
				return 0
			last = stack.pop()
			if not Paired(last, symbol):
				return 0
	if len(stack) != 0:
		return 0 
	return 1


print(solution(string_1))
print('----------------')
print(solution(string_2))
print('----------------')
print(solution(string_3))