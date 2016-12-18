def part1():
	lines = open('day19data.txt').read().split('\n')
	start = ''
	rules = []
	outcomes = set()
	for l in lines:
		if len(l) == 0:
			continue
		elif '=>' in l:
			rules.append(l)
		else:
			start = l
	for r in rules:
		orig,dest=r.split(' => ')
		new = start.replace(orig,dest,1)
		if new in outcomes:
			print(new,"was already present")
		else:
			print(start,"became",new,"with rule",orig,"=>",dest)
			outcomes.add(new)
	return len(outcomes)