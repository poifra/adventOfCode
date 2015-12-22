import sys
def deerProblem(deers):
	timeLimit = 2503
	for deer in deers:
		for t in range(timeLimit):
			if deer['resting']:
				deer['restTime'] += 1
				if deer['restTime'] == deer['rest']:
					deer['resting'] = False
					deer['restTime'] = 0
			else:
				deer['currentPos'] += deer['speed']
				deer['speedTime'] += 1
				if deer['speedDuration'] == deer['speedTime']:
					deer['speedTime'] = 0
					deer['resting'] = True
	return max([x['currentPos'] for x in deers])

def deerPoints(deers):
	timeLimit = 2503
	for t in range(timeLimit):
		for deer in deers:
			if deer['resting']:
				deer['restTime'] += 1
				if deer['restTime'] == deer['rest']:
					deer['resting'] = False
					deer['restTime'] = 0
			else:
				deer['currentPos'] += deer['speed']
				deer['speedTime'] += 1
				if deer['speedDuration'] == deer['speedTime']:
					deer['speedTime'] = 0
					deer['resting'] = True

		far = max([x['currentPos'] for x in deers])
		for deer in deers:
			if deer['currentPos'] == far:
				deer['points'] += 1
			
	return max([x['points'] for x in deers])
	
if __name__ == '__main__':
	with open(sys.argv[1], 'r') as file:
		content = file.read().replace('.','').replace(',','').split('\n')
		deers = []
		for line in content:
			if line[0] != '#':
				name, _, _, speed, _, _ , speedDuration, _, _, _, _, _, _, restDuration, _ = line.split(' ')
				aDeer = {}
				aDeer['name'] = name
				aDeer['speed'] = int(speed)
				aDeer['speedDuration'] = int(speedDuration)
				aDeer['rest'] = int(restDuration)
				aDeer['currentPos'] = 0
				aDeer['resting'] = False
				aDeer['restTime'] = 0
				aDeer['speedTime'] = 0
				deers.append(aDeer)
		print("part 1", deerProblem(deers))
		
		for deer in deers: #reset data
			deer['currentPos'] = 0
			deer['speedTime'] = 0
			deer['restTime'] = 0
			deer['resting'] = False
			deer['points'] = 0
		print("part 2", deerPoints(deers))