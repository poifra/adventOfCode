from itertools import takewhile, islice

def decompress(data, recurse):
	answer = 0
	data = iter(data)
	for c in data:
		if c == '(':
			n, m = map(int, [''.join(takewhile(lambda c: c not in 'x)', data)) for _ in (0, 1)])
			s = ''.join(islice(data, n))
			answer += (decompress(s, recurse) if recurse else len(s))*m
		else:
			answer += 1
	return answer

def part1():
	data = open('day9data.txt').read()
	return decompress(data, False)

def part2():
	data = open('day9data.txt').read()
	return decompress(data, True)