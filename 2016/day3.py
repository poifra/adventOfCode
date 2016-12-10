from itertools import permutations,zip_longest

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def day3part1():
	with open('day3data.txt') as f:
		data = f.read().split('\n')
		valid = 0
		for line in data:
			perms = permutations(map(int,line.split()))
			good = True
			for p in perms:
				if p[0] + p[1] <= p[2]:
					good = False
					break
			valid += good

		return valid


def day3part2():
	with open('day3data.txt') as f:
		groups = grouper(f.read().split('\n'),3)
		valid = 0
		for g in groups:
			good = True
			t1 = permutations(map(int,(g[0].split()[0],g[1].split()[0],g[2].split()[0])))
			t2 = permutations(map(int,(g[0].split()[1],g[1].split()[1],g[2].split()[1])))
			t3 = permutations(map(int,(g[0].split()[2],g[1].split()[2],g[2].split()[2])))
			for p in t1:
				if p[0] + p[1] <= p[2]:
					good = False
					break
			valid += good
			good = True
			for p in t2:
				if p[0] + p[1] <= p[2]:
					good = False
					break
			valid += good
			good = True
			for p in t3:
				if p[0] + p[1] <= p[2]:
					good = False
					break
			valid += good
		return valid
