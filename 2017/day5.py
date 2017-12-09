
def problem():
	# problem description : http://adventofcode.com/2017/day/5
	program = list(map(int,open('day5data.txt','r').read().split('\n')))
	#part 1
	PC = 0
	steps = 0
	while 0 <= PC < len(program):
		steps += 1
		old = PC
		PC += program[PC]
		program[old] += 1
	print("Part 1:",steps)

	#part 2
	PC = 0
	steps = 0
	program = list(map(int,open('day5data.txt','r').read().split('\n')))
	while 0 <= PC < len(program):
		steps += 1
		old = PC
		PC += program[PC]
		if program[old] >= 3:
			program[old] -= 1
		else:
			program[old] += 1

	print("Part 2:",steps)

if __name__ == '__main__':
	problem()