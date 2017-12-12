from functools import reduce
from operator import xor

def hash(numbers, lengths, skipSize=0, currentPos=0):
	size = len(numbers)
	for l in lengths:
		rev = [numbers[(i+currentPos)%size] for i in range(l)][::-1]
		for i,x in enumerate(rev):
			numbers[(currentPos+i) % size] = x

		currentPos = (currentPos + l + skipSize) % size
		skipSize += 1
	return numbers,skipSize,currentPos

def denseHash(sparse):
	blocks =[sparse[i:i+16] for i in range(0,len(sparse), 16)] #get each 16 blocks of 16 digits
	dense = []
	for b in blocks:
		dense.append(reduce(xor, b)) #xor everything
	return dense

def prepareInput(lengths):
	return [ord(i) for i in ",".join(map(str,lengths))] + [17, 31, 73, 47, 23]
		
def sparseHash(asciilengths):
	skipSize = currentPos = 0
	lst = [i for i in range(256)]
	for _ in range(64):
		lst,skipSize,currentPos = hash(lst,asciilengths,skipSize,currentPos)
	return lst

def problem():
	# problem description : http://adventofcode.com/2017/day/10
	lengths = [76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229]
	numbers = [i for i in range(256)]

	#part 1
	h = hash(numbers,lengths)[0]
	print("Part 1 :", h[0]*h[1])
	lengths = []
	#part 2
	print("Part 2 :", bytes(denseHash(sparseHash(prepareInput(lengths)))).hex().lower())

if __name__ == '__main__':
	problem()