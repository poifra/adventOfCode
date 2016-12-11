def part1():
	data = open('day10data.txt').read()
	bots = {}
	outputs = {}
	for line in data:
		if line.startswith('value'):
			words = line.split(' ')
			botid = words[5]
			value = words[1]
			if botid in bots:
				bots[botid] = sorted([int(value),bots[botid]])
			else
				bots[botid] = 
	return decompress(data, False)

def part2():
	data = open('day10data.txt').read()
	return decompress(data, True)