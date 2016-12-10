def has_abba(word):
	return any(a==d and b==c and a!=b for a,b,c,d in zip(x, x[1:], x[2:], x[3:]))

def day7part1():
	with open('day7data.txt') as f:
		data = f.read().split('\n')
		valid = 0
		toggle = itertools.cycle[False,True].__next__
		for line in data:
			form = [(toggle(),line[i]) for i,x in enumerate(line)]
			good = True
			for block in form:
				if has_abba(block[1]) and block[0]:
					good = False
					break
			valid += good
		return valid

def day7part2():
	pass