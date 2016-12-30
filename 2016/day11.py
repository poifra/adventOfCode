from itertools import product, combinations, cycle, permutations
from collections import deque

import sys

def parser(data):
	chips = {}
	generators = {}

	for line_no, line in enumerate(data):
		if 'nothing' in line:
			continue
		words = line.split(' ')
		for i,w in enumerate(words):
			if w.startswith('generator'):
				generator = words[i-1]
				generators[generator] = line_no+1
			elif w.startswith('microchip'):
				chip,_ = words[i-1].split('-')
				chips[chip] = line_no+1
	chip_names = sorted(chips)
	if chip_names != sorted(generators):
		raise Exception('Chip and generator mismatch')

	'''
	State is represented by a 3 tuple composed of 
	elevator_floor, chips_positions, generator_positions
	'''
	initState = 1, tuple(chips[k] for k in chip_names), tuple(generators[k] for k in chip_names)
	finalState = 4,  tuple(4 for _  in chip_names), tuple(4 for _ in generators)

	if not is_valid(initState) or not is_valid(finalState):
		raise Exception('Parsing went to shit')

	return initState, finalState

def is_valid(state):
	elevator, chips, generators = state
	for chip, generator in zip(chips, generators):
		if chip != generator and chip in generators:
			return False #mismatch between chip and generator on a floor

	if any(chip < 1 or chip > 4 for chip in chips):
		return False #everything isnt between floors 1-4

	if any(gen < 1 or chip > 4 for gen in generators):
		return False

	if elevator not in {1,2,3,4}:
		return False #elevator is lost. 

	return True

def get_next_states(state, seen=()):
	elevator, chips, generators = state
	items = list(chips + generators)

	#grab items on elevator floor
	indices = [i for i, item_pos in enumerate(items) if elevator == item_pos]

	#we can take one or two things with us
	indicesChoices = list(combinations(indices,1)) + list(combinations(indices,2))
	
	#we can go up or down
	directions = -1,1
	for indices, direction in product(indicesChoices,directions):
		newElevator = elevator + direction
		newItems = items[:]
		for index in indices:
			newItems[index] += direction
		newChips = newItems[:len(chips)]
		newGens = newItems[len(chips):]

		newState = newElevator, tuple(newChips), tuple(newGens)
		if is_valid(newState) and newState not in seen:
			yield newState


def bfs(init, target):

	def progress(msg, spinner=cycle(r'\|/-')):
		msg = ('\r{}'.format(next(spinner)) + msg)
		sys.stdout.write(msg)
		sys.stdout.flush()

	depth = 0
	queue = deque([(init,depth)])
	seen = {init}
	i = 0
	while queue:
		state, newDepth = queue.popleft()
		i += 1
		if newDepth > depth:
			depth = newDepth
		if state == target:
			return depth
		else:
			if i%2000 == 0:
				progress('search depth {}, queue length {}'.format(newDepth, len(queue)))
		children = list(get_next_states(state,seen))
		seen.update(children)
		queue.extend((child, depth+1) for child in children) 

def part1(extraThings = False):
	f = open('day11data.txt').read().split('\n')
	init, target = parser(f)
	if not extraThings:
		return bfs(init, target)
	else:
		init = init[0], init[1] + (1,1), init[2] + (1,1)
		target = target[0], target[1] + (4,4), target[2] + (4,4)
		return bfs(init,target)

def part2():
	return part1(True)

if __name__ == '__main__':
	import time
	start = time.time()
	print(part1())
	print("Part 1 took ",time.time()-start,"seconds")
	start = time.time()
	print(part2())
	print("Part 2 took", time.time()-start,"seconds")