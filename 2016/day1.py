def day1part1():
	with open('day1data.txt') as f:
		data = f.read().replace(' ','').split(',')
		pos = [0,0]
		face = 0
		for d in data:
			if d[0] == 'R':
				face = (face+1)%4
			else:
				face = (face-1)%4

			amount = int(d[1:])
			if face == 0:
				pos[1] += amount
			if face == 1:
				pos[0] -= amount
			if face == 2:
				pos[1] -= amount
			if face == 3:
				pos[0] += amount
		return sum(map(abs,pos))

def day1part2():
	with open('day1data.txt') as f:
		data = f.read().replace(' ','').split(',')
		pos = [0,0]
		visited = [pos[:]]
		face = 0
		for d in data:
			if d[0] == 'R':
				face = (face-1)%4
			else:
				face = (face+1)%4

			amount = int(d[1:])
			for _ in range(amount):
				if face == 0:
					pos[1] += 1
				elif face == 1:
					pos[0] -= 1
				elif face == 2:
					pos[1] -= 1
				elif face == 3:
					pos[0] += 1
				if pos in visited:
					return sum(map(abs,pos))
				else:
					visited.append(pos[:])