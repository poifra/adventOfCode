def day2part1():
	with open('day2data.txt') as f:
		data = f.read().split('\n')
		keypad = [
			[1,2,3],
			[4,5,6],
			[7,8,9]
			]
		code = ''
		start = [1,1]
		for hint in data:
			for c in hint:
				if c == 'U':
					start[0] -= 1 if start[0] > 0 else 0
				if c == 'L':
					start[1] -= 1 if start[1] > 0 else 0
				if c == 'R':
					start[1] += 1 if start[1] < 2 else 0
				if c == 'D':
					start[0] += 1 if start[0] < 2 else 0
			code += str(keypad[start[0]][start[1]])
		return code

def day2part2():
	with open('day2data.txt') as f:
		data = f.read().split('\n')
		keypad = [
			[None,None,1,None,None],
			[None,2,3,4,None],
			[5,6,7,8,9],
			[None,'A','B','C',None],
			[None,None,'D',None,None]
			]
		code = ''
		start = [2,0]
		for hint in data:
			for c in hint:
				line = start[0]
				col = start[1]
				if c == 'U':
					start[0] -= 1 if start[0] > 0 and keypad[line-1][col] is not None else 0
				if c == 'L':
					start[1] -= 1 if start[1] > 0 and keypad[line][col-1] is not None else 0
				if c == 'R':
					start[1] += 1 if start[1] < 4 and keypad[line][col+1] is not None else 0
				if c == 'D':
					start[0] += 1 if start[0] < 4 and keypad[line+1][col] is not None else 0
			code += str(keypad[start[0]][start[1]])
		return code