def nextCheck(chr_iter):
	for c in chr_iter:
		yield '1' if c == next(chr_iter) else '0'

def part1(data='10111011111001111', size = 272):
	#data = '10000'
	#size = 20
	a = data
	while len(a) < size:
		a += '0'+a[::-1].replace('0', '2').replace('1', '0').replace('2', '1')
	a = a[:size]
	while len(a) % 2 == 0:
		a = ''.join(nextCheck(iter(a)))
	return a

def part2():
	return part1(size=35651584)
 
if __name__ == '__main__':
	import time
	assert part1('10000',20) == '01100'
	start = time.time()
	print(part1())
	print("time for part 1 :",time.time()-start)
	start = time.time()
	print(part2())
	print("time for part2 :",time.time()-start)