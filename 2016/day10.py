from collections import defaultdict

def part1(part2=False):
	data = open('day10data.txt').read().split('\n')
	bots = defaultdict(set)
	outputs = defaultdict(set)

	botid = []
	done = set()

	while len(done) < len(data):
		for l in data:
			if l in done:
				continue

			line = l.split(' ')

			if line[0] == 'value':
				val,dest = map(int,[line[1], line[5]])
				bots[dest].add(val)
				done.add(l)
				continue

			source = int(line[1])

			nums = bots[source]
			if 61 in nums and 17 in nums:
				botid = source
			if len(nums) < 2:
				continue

			lo = min(nums)
			hi = max(nums)
			loDest = int(line[6])
			hiDest = int(line[11])
			if line[5] == 'output':
				outputs[loDest].add(lo)
			else:
				bots[loDest].add(lo)

			if line[10] == 'output':
				outputs[hiDest].add(hi)
			else:
				bots[hiDest].add(hi)

			done.add(l)
	if part2:
		return outputs[0].pop()*outputs[1].pop()*outputs[2].pop()
	else:
		return botid
def part2():
	return part1(True)