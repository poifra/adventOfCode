'''
This has nothing to do with Sean Plott
'''
import sys
from itertools import permutations as perm

def hamPath(pairs, mode):
	'''
	returns shortest or longest hamiltonian path in non-oriented graph given by pairs
	'''
	allDist = []

	for x in perm(pairs):
		allDist.append(sum(pairs[x[i]][x[i+1]] for i in range(len(x) - 1)))
	return min(allDist) if mode == 'min' else max(allDist)

if __name__ == "__main__":
	testDistances = {'london':dict(), 'dublin':dict(), 'belfast':dict()}
	testDistances['london']['dublin'] = testDistances['dublin']['london'] = 464
	testDistances['london']['belfast'] = testDistances['belfast']['london'] = 518
	testDistances['dublin']['belfast'] = testDistances['belfast']['dublin'] = 141
	assert hamPath(testDistances, 'min') == 605
	assert hamPath(testDistances, 'max') == 982
	dayData = sys.argv[1]
	with open(dayData, 'r') as file:
		content = file.read().split('\n')
		distances = dict()
		places = set()
		for line in content:
			start, _, end, _, value = line.split(' ')
			places.add(start)
			places.add(end)
			distances.setdefault(start, dict())[end] = int(value)
			distances.setdefault(end, dict())[start] = int(value) #since the graph is not oriented
		print("shortest", hamPath(distances, 'min'))
		print("longest", hamPath(distances, 'max'))
		