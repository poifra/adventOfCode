def part1():
#	data = "5-8\n0-2\n4-7"
	data = open('day20data.txt').read().split('\n')
#	data = data.split('\n')
	banned = []
	for line in data:
		lo,hi = map(int,line.split("-"))
		for i in range(lo,hi+1):
			banned.append(i)
	banned = sorted(banned)
	for i in range(len(banned)-1):
		if banned[i]+1 != banned[i+1]:
			return banned[i]+1 