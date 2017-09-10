# Works 100%

odd_list = [9,3,9,3,9,7,9]

def unpairedValue(items_list):
	N = len(items_list)
	for item in range(N):
		if items_list.count(items_list[item]) % 2:
			return items_list[item]



print(unpairedValue(odd_list))