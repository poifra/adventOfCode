def isNice(input):
	#not a single regex was given that day
	from re import match
	if("ab" in input or "cd" in input or "pq" in input or "xy" in input):
		return False
	if(input.count('a')+input.count('e')+input.count('i')+input.count('o')+input.count('u') < 3):
		return False
	for i in range(len(input)-1):
		if(input[i] == input[i+1]):
			return True
	return False
	
def isMoreNice(input):
	found = False
	for i in range(len(input)-2):
		if(input[i] == input[i+2]):
			found = True
			break
			
	if(not found):
		return False #1st condition not met
		
	for i in range(len(input)-1):
		if(input.count(input[i]+input[i+1]) >= 2):
			return True
	return False

if(__name__=='__main__'):
	import sys
	dayData = sys.argv[1]
	def part1():
		assert(isNice("ugknbfddgicrmopn"))
		assert(isNice("aaa"))
		assert(not isNice("jchzalrnumimnmhp"))
		assert(not isNice("haegwjzuvuyypxyu"))
		assert(not isNice("dvszwmarrgswjxmb"))
		with open(dayData,"r") as f:
			total = 0
			content = f.read().split("\n")
			for line in content:
				if(isNice(line)):
					total += 1
			return total
	def part2():
		assert(isMoreNice("qjhvhtzxzqqjkmpb"))
		assert(isMoreNice("xxyxx"))
		assert(not isMoreNice("uurcxstgmygtbstg"))
		assert(not isMoreNice("ieodomkazucvgmuy"))
		with open(dayData,"r") as f:
			total = 0
			content = f.read().split("\n")
			for line in content:
				if(isMoreNice(line)):
					total += 1
			return total
			
	print("part1",part1())
	print("part2",part2())