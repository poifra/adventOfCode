def part1(registers ={'a':0,'b':0,'c':0,'d':0}):
	data = open('day12data.txt').read().split('\n')
	
	current = 0
	while current < len(data):
		line = data[current]
		words = line.split(' ')
		#print("line =",line, "current inst =",current+1, "registers :",registers)
		if line.startswith('cpy'):
			src = words[1]
			dst = words[2]
			if src.isdigit():
				registers[dst] = int(src)
			else:
				registers[dst] = registers[src]

		target = words[1]

		if line.startswith('inc'):
			registers[target] += 1
		if line.startswith('dec'):
			registers[target] -= 1
		jumpAmnt = 1
		if line.startswith('jnz'):
			if target.isdigit() and int(target) != 0:
				jumpAmnt = int(words[2])
			else:
				if registers[target] != 0:
					jumpAmnt = int(words[2])
		current += jumpAmnt
	return registers['a']

def part2():
	return part1({'a':0,'b':0,'c':1,'d':0})

if __name__=='__main__':
	part2()