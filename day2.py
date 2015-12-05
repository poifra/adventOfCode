
def calcPaper(dimensions):
	l,w,h=dimensions[0],dimensions[1],dimensions[2]
	size1=int(l)*int(w)
	size2=int(w)*int(h)
	size3=int(l)*int(h)
	smallestSide = min(size1,size2,size3)
	return 2*size1 + 2*size2 + 2*size3 + smallestSide

def calcRibbon(dimensions):
	l,w,h=int(dimensions[0]),int(dimensions[1]),int(dimensions[2])
	volume = l*w*h
	perim1=2*l+2*h
	perim2=2*l+2*w
	perim3=2*w+2*h
	smallest = min(perim1,perim2,perim3)
	return volume+smallest

if(__name__=='__main__'):
	import sys
	def part1():
		assert (calcPaper("2x3x4".split("x")) == 58)
		assert (calcPaper("1x1x10".split("x")) == 43)
		dayData = sys.argv[1]
		with open(dayData,"r") as f:
			total = 0
			content = f.read().split("\n")
			for line in content:
				total += calcPaper(line.split("x"))
			return total
	def part2():
		assert (calcRibbon("2x3x4".split("x")) == 34)
		assert (calcRibbon("1x1x10".split("x")) == 14)
		dayData = sys.argv[1]
		with open(dayData,"r") as f:
			total = 0
			content = f.read().split("\n")
			for line in content:
				total += calcRibbon(line.split("x"))
			return total
			
	print("part1",part1())
	print("part2",part2())