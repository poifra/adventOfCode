import sys
import itertools
def tsPath(pairs):
	allHappinesses = []
	allValues = []
	for x in itertools.permutations(pairs):
		sub = list(x)
		sub.append(x[0])
		allHappinesses.append(sub)
		
	for setup in allHappinesses:
		setupValue = 0
		for i in range(len(setup)-1):
			setupValue += pairs[setup[i]][setup[i+1]]+pairs[setup[i+1]][setup[i]]
		allValues.append(setupValue)
#		print(setup,setupValue)
	return max(allValues)
	
if __name__ == '__main__':
	with open(sys.argv[1], 'r') as file:
		content = file.read().replace('.','').split('\n')
		happinesses = {}
		for line in content:
			human1,_,mood,value,_,_,_,_,_,_,human2 = line.split(' ') #hurrah for tuples
			if mood == 'gain':
				happinesses.setdefault(human1,dict())[human2] = int(value)
			else:
				happinesses.setdefault(human1,dict())[human2] = - int(value) #loss of happiness
		
		print("part1", tsPath(happinesses))
		
		for people in happinesses.keys():
			happinesses[people]['FP'] = 0
		happinesses['FP'] = dict()
		for people in happinesses.keys()-'FP': #dont want to be happy with myself
			happinesses['FP'][people] = 0
			
		print("part2", tsPath(happinesses))