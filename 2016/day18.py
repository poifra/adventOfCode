def part1():
	current = open('day18data.txt').read()
	size = 40
	room = [''*len(current) for i in range(size)]
	for i in range(1, size):
		for j in range(1,len(current)):
			left = right = center = -1
			