from itertools import combinations

def problem():
	# problem description : http://adventofcode.com/2017/day/2
	#part 1
	text = open('day2data.txt','r').read().replace('\t',' ').split('\n')

	#assuming all lines have the same amount of numbers
	lineCount = len(text)
	colCount = len(text[0].split(' '))
	data = [[int(text[j].split(' ')[i]) for i in range(lineCount)] for j in range(colCount)]

	checksum = 0
	for line in data:
		checksum += max(line) - min(line)
	print ("Part 1 :", checksum)

	checksum = 0
	for line in data:
		pairs = combinations(line,2)
		for p in pairs:
			mx, mi = max(p), min(p)
			if mx%mi == 0:
				checksum += int(mx/mi)
				break
	print ("Part 2 :", checksum) 


if __name__ == '__main__':
	problem()