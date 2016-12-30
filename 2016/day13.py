INPUT = 1352
SIZE = 50
def isWall(x,y):
	num = x*x + 3*x + 2*x*y + y + y*y + INPUT
	return bin(num).count('1') % 2 == 1

from collections import deque

def pprint(maze):
	for x in range(SIZE):
		for y in range(SIZE):
			print(maze[x][y],end='')
		print('\n',end='')
	print('\n')

def buildMaze():
	return [['#' if isWall(x,y) else '.' for x in range(SIZE)] for y in range(SIZE)]

def get_next_states(state,maze,seen=()):
	dirs = {(0,1),(0,-1),(1,0),(-1,0)}
	for d in dirs:
		newState = 
		if is_valid(newState, maze) and newState not in seen

def bfs(maze):
	xGoal = 31
	yGoal = 39
	depth = 0
	start = (1,1)
	queue = deque([start,depth])
	seen = {start}
	i = 0
	while queue:
		state,newDepth = queue.popleft()
		i+=1
		if newDepth > depth:
			depth = newDepth
		if state[0] == xGoal and state[1] == yGoal:
			return depth

		children = list(get_next_states(state,maze,seen))
		seen.update(children)
		queue.extend((child, depth+1) for child in children)

def part1():
	bfs(maze)