def part1():
	current = open('day18data.txt').read()
	height = 40
	width = len(current)
	room = [['.' for _ in range(width)] for _ in range(height)]
	room[0] = list(current)