from functools import lru_cache

fibonacci_cache = {}

def fibonacci(n):
	if n in fibonacci_cache:
		return fibonacci_cache[n]

	if n == 1:
		value = 1
	if n == 2:
		value = 2
	elif n > 2:
		value = fibonacci(n-1) + fibonacci(n - 2)
	fibonacci_cache[n] = value
	return value


# ------------------------
# with decorator in use

@lru_cache(maxsize = 10000)
def fibonacci_dec(n):
	if n == 1:
		return 1
	if n == 2:
		return 2
	elif n > 2:
		return fibonacci(n-1) + fibonacci(n - 2)


for n in range (1, 1001):
	print(fibonacci_dec(n))