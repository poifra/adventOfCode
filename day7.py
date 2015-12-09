VALUES = {}
PARTS = {}

def gator(instruction):
	'''
	Recursion ftw!
	'''
	if instruction in VALUES:
		return VALUES[instruction]
	if instruction.isdigit():
		return int(instruction)
	
	value = PARTS[instruction]
	
	if 'NOT' in value:
		a = value.split(' ')[1]
		return ~ gator(a)
		
	try:
		a,op,b = value.split(' ')
		
		#cache intermediate values to avoid computing them while(1) : comment += 'and over '
		res_a = gator(a)
		VALUES[a] = res_a
		
		res_b = gator(b)
		VALUES[b] = res_b
		
		if op == 'AND':
			res = gator(a) & gator(b)
		elif op == 'OR':
			res = gator(a) | gator(b)
		elif op == 'RSHIFT':
			res = gator(a) >> gator(b)
		elif op == 'LSHIFT':
			res = gator(a) << gator(b)
			
		return res
		
	except ValueError:
		return gator(value)
		
if(__name__=='__main__'):
	import sys
	dayData = sys.argv[1]

	def part1():
		'''
		Solves part 1 which is find the value of wire 'a'
		'''
		with open(dayData,"r") as f:
			content = f.read().split("\n")
			content.sort()
			for line in content:
				operation, dest = line.split(' -> ')
				PARTS[dest] = operation
			return gator('a')
	def part2():
		'''
		feeling of deja-vu
		'''
		with open(dayData,"r") as f:
			content = f.read().split("\n")
			content.sort()
			for line in content:
				operation, dest = line.split(' -> ')
				PARTS[dest] = operation
			aValue = gator('a')
			global VALUES
			VALUES = {} #reset
			PARTS['b'] = str(aValue) #override previous value for 'b'
			return gator('a')
		
	print("part1",part1())
	print("part2",part2())