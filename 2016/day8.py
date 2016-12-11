def ppGrid(grid):
	for line in grid:
		for n in line:
			print(n,end='')
		print('\n',end='')

def printscreen(screen):
	import sys
	# clear the terminal
	sys.stdout.write('\033c')

	ssize = len(screen[0])

	print('┍{}┑'.format('━' * ssize))
	for row in screen:
		sys.stdout.write('│')
		for px in row:
			sys.stdout.write('{}'.format(px))
		sys.stdout.write('│\n')
	print('┕{}┙'.format('━' * ssize))

def day8part1():
	screen = [['.' for i in range(50)] for j in range(6)]
	with open('day8data.txt') as f:
		lines = f.read().split('\n')

		for l in lines:
			import time
			time.sleep(0.2)
			printscreen(screen)
			if l.startswith('rect'):
				words = l.split(' ')
				dim = words[1].split('x')
				width = int(dim[0])
				height = int(dim[1])
				for h in range(height):
					for r in range(width):
						screen[h][r] = '#' 
			else:
				words = l.split(' ')
				amount = int(words[-1])
				toShift = int(words[2].split('=')[-1])
				if l.startswith('rotate row'):
					row = screen[toShift]
					row = [row[(i-amount)%len(row)] for i in range(50)] 
					screen[toShift] = row

				if l.startswith('rotate column'):
					col = [screen[i][toShift] for i in range(6)]
					col = [col[(i-amount)%len(col)] for i in range(6)]
					for i in range(6):
						screen[i][toShift] = col[i]
	count = 0
	for line in screen:
		for c in line:
			if c == '#':
				count += 1
	printscreen(screen)
	return count 
def day8part2():
	day8part1()