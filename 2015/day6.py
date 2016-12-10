def lights(input, grid, brightLights, returnSum=False):
	instructions = input.split(" ")
	if(instructions[0] == "turn"):
		startCoords, endCoords = instructions[2],instructions[4]
		start = startCoords.split(",")
		end = endCoords.split(",")
		xStart = int(start[0])
		yStart = int(start[1])
		xEnd = int(end[0])
		yEnd = int(end[1])
		if(instructions[1] == "off"):
			for x in range(xStart,xEnd+1): # +1 because inclusive end
				for y in range(yStart, yEnd+1):
					if(brightLights):
						grid[x][y] = max(0, grid[x][y] -1) #prevents going below 0
					else:
						grid[x][y] = 0
		else: #turn on
			for x in range(xStart,xEnd+1):
				for y in range(yStart, yEnd+1):
					if(brightLights):
						grid[x][y] += 1
					else:
						grid[x][y] = 1
	else: #toggle mode
		startCoords, endCoords = instructions[1],instructions[3]
		start = startCoords.split(",")
		end = endCoords.split(",")
		xStart = int(start[0])
		yStart = int(start[1])
		xEnd = int(end[0])
		yEnd = int(end[1])
		for x in range(xStart,xEnd+1):
			for y in range(yStart,yEnd+1):
				if(brightLights):
					grid[x][y] += 2
				else:
					grid[x][y] ^= 1 #flip bit with xor
	if(returnSum):
		return sum(map(sum,grid))

def clearGrid(grid):
	for x in range(len(grid)):
		for y in range(len(grid[0])):
			grid[x][y] = 0
			
if(__name__=='__main__'):
	import sys
	dayData = sys.argv[1]
	size = 1000
	def part1():
		grid = [[0 for i in range(size)] for j in range(size)]
		assert(lights("turn on 0,0 through 999,999",grid,False,True) == 1000000)
		assert(lights("toggle 0,0 through 999,0",grid,False,True) == 1000000-1000)
		assert(lights("turn off 499,499 through 500,500",grid,False,True) == 1000000-1000-4)
		clearGrid(grid)
		with open(dayData, "r") as f:
			content = f.read().split("\n")
			for line in content:
				lights(line,grid,False)
			return sum(map(sum,grid))
	def part2():
		grid = [[0 for i in range(size)] for j in range(size)]
		assert(lights("turn on 0,0 through 0,0",grid,True,True) == 1)
		assert(lights("toggle 0,0 through 999,999",grid,True,True) == 2000001)
		clearGrid(grid)
		with open(dayData, "r") as f:
			content = f.read().split("\n")
			for line in content:
				lights(line,grid,True)
			return sum(map(sum,grid))
	print("part1",part1())
	print("part2",part2())