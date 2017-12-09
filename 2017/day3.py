import math

def distance(n):
	i=1
	while i**2 < n:
		i += 2
	pivots =  [i*i - k*(i-1) for k in range(4)]
#	print("Pivots for",i,pivots)
	for p in pivots:
		dist = abs(p-n)
	#	print(n,"is",dist,"away from",p)
		if dist <= (i-1)//2:
			return i-1-dist


def problem():
	# problem description : http://adventofcode.com/2017/day/3
	data = 325489

	#part 1
	assert distance(1) == 0
	assert distance(12) == 3
	assert distance(23) == 2
	assert distance(1024) == 31
	print ("Part 1:",distance(data))

	#part 2
	#if there's a sequence, it's in the OEIS
	#https://oeis.org/A141481/b141481.txt

if __name__ == '__main__':
	problem()