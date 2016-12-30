registers = {'a':7,'b':0,'c':0,'d':0}
PC = 0
program = open('day23data.txt').read().split('\n')

def inc(arg):
	if arg in registers:
		registers[arg] += 1

def dec(arg):
	if arg in registers:
		registers[arg] -= 1

def cpy(src, dst):
	if src in registers and dst in registers:
			registers[dst] = registers[src]
	elif dst in registers:
			registers[dst] = int(src)

def jnz(check, amount):
	global PC
	
	if check in registers:
		check = registers[check]
	else:
		check = int(check)

	if amount in registers:
		amount = registers[amount]
	else:
		amount = int(amount)

	if check != 0:
		PC += amount-1

def tgl(arg):
	global program
	if arg in registers:
		target = PC + registers[arg]
	else:
		target = PC + int(arg)

	if target < 0 or target >= len(program):
		return
	toChange = program[target]
	words = toChange.split(' ')
	if len(words) == 2:
		if words[0] == 'inc':
			words[0] = 'dec'
		else:
			words[0] = 'inc'
	else:
		if words[0] == 'jnz':
			words[0] = 'cpy'
		else:
			words[0] = 'jnz'
	newInstr = ' '.join(words)
	program[target] = newInstr


def part1(part2=False):
	if part2:
		registers['a'] = 12
	instructions = {
					'inc':inc,
					'dec':dec,
					'cpy':cpy,
					'jnz':jnz,
					'tgl':tgl
					}
	global PC
	while PC < len(program):
		current = program[PC]
		words = current.split(' ')
		if len(words) == 2:
			instructions[words[0]](words[1])
		else:
			instructions[words[0]](words[1],words[2])
		PC += 1
	return registers['a']

if __name__=='__main__':
	part1()

def part2():
	return part1(True)