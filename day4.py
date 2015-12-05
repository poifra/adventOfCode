def magicNumber(input):
#bruteforce ftw
	from hashlib import md5
	for i in range(10000000):
		if(md5((input+str(i)).encode()).hexdigest()[:5] == "00000"):
			return i
			
def magicNumber6(input):
	from hashlib import md5
	for i in range(10000000):
		if(md5((input+str(i)).encode()).hexdigest()[:6] == "000000"):
			return i

if(__name__=="__main__"):
	input = "bgvyzdsv"
	def part1():
		assert (magicNumber("abcdef") == 609043)
		assert (magicNumber("pqrstuv") == 1048970)
		return magicNumber(input)
	def part2():
		return magicNumber6(input)
		
	print("part1",part1())
	print("part2",part2())