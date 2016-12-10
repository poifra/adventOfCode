from collections import Counter

def day6part1():
	with open('day6data.txt') as f:
		data = f.read().split('\n')
		return ''.join(Counter(x).most_common()[0][0] for x in zip(*data))


def day6part2():
	with open('day6data.txt') as f:
		data = f.read().split('\n')
		return ''.join(Counter(x).most_common()[-1][0] for x in zip(*data))