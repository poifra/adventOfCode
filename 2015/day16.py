import sys

def matchSue(sues, infos)
	return goodSue

if __name__ == '__main__':
	with open(sys.argv[1], 'r') as file:
		lines = file.read().strip(':').strip(',').split('\n')
		infos = []
		for line in lines:
			aSue = {}
			(_, id, hint1, value1, hint2, value2, hint3, value3) = line.split(' ')
			aSue['id'] = int(id)
			aSue[hint1] = int(value1)
			aSue[hint2] = int(value2)
			aSue[hint3] = int(value3)
			infos.append(aSue)