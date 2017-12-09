from itertools import combinations
def valid(txt):
	words = txt.split(' ')
	knownWords = []
	for w in words:
		if w in knownWords:
			return False
		knownWords.append(w)
	return True

def validAnagram(txt):
	pairs = combinations(txt.split(' '),2)
	for p in pairs:
		if sorted(p[0]) == sorted(p[1]):
			return False
	return True

def problem():
	# problem description : http://adventofcode.com/2017/day/4
	data = open('day4data.txt','r').read().split('\n')
	#part 1
	assert valid("aa bb cc dd ee") == True
	assert valid("aa bb cc dd aa") == False
	assert valid("aa bb cc dd aaa") == True

	count = 0
	for phrase in data:
		if valid(phrase):
			count += 1
	print("Part 1:",count)

	#part 2
	assert validAnagram("abcde fghij") == True
	assert validAnagram("abcde xyz ecdab") == False
	assert validAnagram("a ab abc abd abf abj") == True
	assert validAnagram("iiii oiii ooii oooi oooo") == True
	assert validAnagram("oiii ioii iioi iiio") == False
	
	count = 0
	for phrase in data:
		if validAnagram(phrase):
			count += 1
	print("Part 2:",count)


if __name__ == '__main__':
	problem()