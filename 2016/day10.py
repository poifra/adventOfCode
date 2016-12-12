def part1():
	data = open('day10data.txt').read().split('\n')
	bots = {}
	outputs = {}
	while data:
		if line.startswith('value'):
			words = line.split(' ')
			botid = words[5]
			value = words[1]
			if botid in bots:
				bots[botid] = sorted([int(value),bots[botid]])
			else
				bots[botid] = int(value)
	return decompress(data, False)

def part2():
	data = open('day10data.txt').read()
	return decompress(data, True)