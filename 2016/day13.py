SIZE = 50
def isWall(x,y):
	f = x*x + 3*x + 2*x*y + y + y*y + 1352
	return bin(f).count('1') % 2 == 1

def buildMaze():
	lst = [['.' for _ in range(SIZE)] for _ in range(SIZE)]
	for i in range(SIZE):
		for j in range(SIZE):
			if isWall(i,j):
				lst[i][j] = '#'
	return lst

def solve(maze, x, y):
	if x == 31 and y == 39:
		maze[x][y] = '0'
		return True
	if maze[x][y] == '#':
		return False #already visited or its a wall
	maze[x][y] = 'o' #current is marked
	if x+1 <= SIZE and maze[x+1][y] == '.':
		return solve(maze,x+1,y)
	if x-1 >= 0 and maze[x-1][y] == '.':
		return solve(maze,x-1,y)
	if y+1 <= SIZE and maze[x][y+1] == '.':
		return solve(maze,x,y+1)
	if y-1 >= 0 and maze[x][y-1] == '.':
		return solve(maze, x, y-1)
	maze[x][y] = ' '
def pprint(maze):
	for i in range(SIZE):
		for j in range(SIZE):
			print(maze[i][j], end='')
		print()
def part1():
	maze = buildMaze()
	solve(maze,1,1)
	pprint(maze)