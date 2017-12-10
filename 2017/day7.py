
def problem():
	# problem description : http://adventofcode.com/2017/day/7
	memory = [11,11,13,7,0,15,5,5,4,4,1,1,7,1,15,11]
	#memory = [0,2,7,0] #test input
	size = len(memory)
	seen = []
	
	#part 1
	while not memory in seen:
		seen.append(memory[:])
		top = max(memory)
		i = memory.index(top)
		memory[i] = 0
		while top:
			top -= 1
			memory[(i+1) % size] += 1
			i += 1
		#print(memory)

	print("Part 1",len(seen))
	#part 2
	print("Part 2",len(seen) - seen.index(memory))

if __name__ == '__main__':
	problem()