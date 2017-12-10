from collections import defaultdict
def problem():
	d = defaultdict(int)
	#part 1
	#one liners are cool
	exec(open('day8data.txt', 'r').read().replace('inc','+=').replace('dec','-=').replace('\n',' else 0\n'),{},d)
	print("part 1 :", max(d.values()))

	#part 2
	data = open('day8data.txt', 'r').read().replace('inc','+=').replace('dec','-=').replace('\n',' else 0\n').split('\n')
	d = defaultdict(int)
	maxVal = 0
	for line in data:
		exec(line,{},d)
		currentMax = max(d.values())
		if currentMax > maxVal:
			maxVal = currentMax

	print ("part 2 :",maxVal)

if __name__ == '__main__':
	problem()