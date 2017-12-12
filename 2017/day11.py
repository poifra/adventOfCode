def dist(directions, keepMax = False):
	directions = directions.split(',')
	maxDist = 0
	x = y = z = 0
	for d in directions:
		if d == 'n':
			y += 1
			z -= 1
		if d == 'ne':
			x += 1
			z -= 1
		if d == 'se':
			x += 1
			y -= 1
		if d == 's':
			z += 1
			y -= 1
		if d == 'sw':
			z += 1
			x -= 1
		if d == 'nw':
			y += 1
			x -= 1
		current = (abs(x)+abs(y)+abs(z))//2
		if keepMax and current > maxDist:
			maxDist = current
	
	if keepMax:
		return maxDist
	else:
		return current

def problem():
	# problem description : http://adventofcode.com/2017/day/11
	directions = open('day11data.txt','r').read().strip('\n')
	#part 1
	assert dist("ne,ne,ne") == 3
	assert dist("ne,ne,sw,sw") == 0
	assert dist("ne,ne,s,s") == 2
	assert dist("se,sw,se,sw,sw") == 3
	print ("Part 1: ",dist(directions))

	#part 2
	print("Part 2:", dist(directions,keepMax=True))

if __name__ == '__main__':
	problem()