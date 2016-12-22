def part1():
	lines = open('day22data.txt').read().split('\n')
	disks = []
	for l in lines:
		coord,size,used,avail = l[:4]
