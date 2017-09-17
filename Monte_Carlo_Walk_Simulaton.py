import random

number_of_walks = 1000
max_distance = 7

def random_walk(n):
	x, y = 0, 0
	for i in range(n):
		(dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
		x += dx
		y += dy
	return(x, y)

for walk_length in range(1, 100):
	no_tansport = 0 # Number of walks 4 or fewer blocks from home
	for i in range(number_of_walks):
		(x, y) = random_walk(walk_length)
		distance = abs(x) + abs(y)
		if distance <= max_distance:
			no_tansport += 1
	no_transport_percentage = float(no_tansport) / number_of_walks
	print('Walk size = ', walk_length,
	 'with ', round(100*no_transport_percentage, 2),
	 ' % chance of transport home')


