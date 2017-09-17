import math
import time

def is_prime(n):
	if n == 1:
		return False
	if n == 2:
		return True
	if n > 2 and n % 2 == 0:
		return False
	max_divisor = math.floor(math.sqrt(n))
	for d in range(3, 1 + max_divisor, 2):
		if n % d == 0:
			return False
	return True

# ==== Computation Time ====
t0 = time.time()
for n in range(1, 1000000):
	is_prime(n)
t1 = time.time()
print('Compotation time is: ', t1 - t0)