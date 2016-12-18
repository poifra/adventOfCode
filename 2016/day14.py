import hashlib

computed = {}

def longMD5(s):
	h = s
	for _ in range(2017):
		h = hashlib.md5(bytes(h,'utf-8')).hexdigest()
	return h

def shortMD5(s):
	return hashlib.md5(bytes(s,'utf-8')).hexdigest()

def has3(s):
	#returns true if any 3 consecutives characters in given string are the same
	for a,b,c in zip(s, s[1:], s[2:]):
		if a==b==c:
			return a,True
	return None,False

def genNext1000(func, data, index):
	numbers = [i for i in range(index+1,index+1001)]
	lst = []
	for i in numbers:
		if i in computed:
			lst.append(computed[i])
		else:
			res = func(data+str(i))
			computed[i] = res
			lst.append(res)

	return lst

def part1(manyTimes = False):
	func = longMD5 if manyTimes else shortMD5
	data = 'jlmsuwbz'
	#data = 'abc'
	hashes = []
	index = 0
	while len(hashes) != 64:
		if index in computed:
			code = computed[index]
		else:
			code = func(data+str(index))
			computed[index] = code
		letter,suit = has3(code)
		if suit:
			next1000 = genNext1000(func, data, index)
			for n in next1000:
				if letter*5 in n:
					hashes.append([index, n])
					break
		index += 1
	return hashes[-1][0]

def part2():
	return part1(True)

if __name__=='__main__':
	print(part1())
	computed = {} #c
	print(part2())