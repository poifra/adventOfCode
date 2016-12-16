def convert(a):
	b = a[::-1] #reverse
	b = b.replace('0', '2').replace('1', '0').replace('2', '1')
	return a + '0' + b
def part1(size = 272):
	data = '10111011111001111'
	#data = '10000'
	#size = 20
	a = data
	while len(a) < size:
	#	print(a,"is still too short len =",len(a))
		a = convert(a)
	#print(a, 'is long enough len =',len(a))
	a = a[:size] #keep only the data we need
	#print("The first",size,"chars are", a)
	while len(a) % 2 == 0:
		a = ''.join(['1' if b[0] == b[1] else '0' for b in [a[i:i+2] for i  in range(0,len(a),2)]])
		#print('checksum is now',a,"of length",len(a))
	return a

def part2():
	return part1(35651584)

if __name__ == '__main__':
	import time
	start = time.time()
	part1()
	print("time for part 1 :",time.time()-start)
	start = time.time()
	part2()
	print("time for part2 :",time.time()-start)