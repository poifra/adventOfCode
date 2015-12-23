import itertools

def containers(input):
	'''
	brute force is love, 
	brute force is live
	'''
	count = 0
	#this could probably be a sweet sweet one liner
	for size in range(1,len(input)):
		for x in itertools.combinations(input,size):
			if sum(x) == 150:
				count += 1
	return count 
	
def minimumContainers(input):
	count = 0
	minSize = 0
	for size in range(1,len(input)):
		for x in itertools.combinations(input,size):
			if sum(x) == 150:
				minSize = size
				break
		if minSize != 0:
			break;
	for x in itertools.combinations(input,minSize):
		if sum(x) == 150:
			count += 1
			
	return count

if __name__ == '__main__':
	with open('day17data.txt', 'r') as file:
		numbers = [int(x) for x in file.read().split('\n')]
		print("part 1", containers(numbers))
		print("part 2", minimumContainers(numbers))