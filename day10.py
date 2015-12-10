from itertools import groupby

def lookAndSay(input):
	'''
	glorious itertools
	'''
	subGroups = [list(g) for _,g in groupby(input)]
	result = ""
	for sub in subGroups:
		result += str(len(sub)) + sub[0]
	return result
	
if __name__ == '__main__':
	#test cases
	assert lookAndSay('1') == '11'
	assert lookAndSay('11') == '21'
	assert lookAndSay('21') == '1211'
	assert lookAndSay('1211') == '111221'
	assert lookAndSay('111221') == '312211'
	
	res = '3113322113' #input
	nbIter = 40 #change at will
	for _ in range(nbIter):
		res = lookAndSay(res)
	print(res) #for fun, but its not going to be pretty
	print(len(res))
	