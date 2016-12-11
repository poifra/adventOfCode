import itertools
import re

def has_abba(word):
	return any(a==d and b==c and a!=b for a,b,c,d in zip(word, word[1:], word[2:], word[3:]))

def day7part1():
	with open('day7data.txt') as f:
		data = f.read().split('\n')
		valid = 0
		for line in data:
			line = line.replace('[',']').split(']')
			toggle = itertools.cycle([False,True]).__next__
			form = [(toggle(),line[i]) for i,x in enumerate(line)]
			good = True
			found = False
			for block in form:
				if not good:
					break
				if has_abba(block[1]):
					if block[0]:
						good = False
					else:
						found = True
			valid += (good and found)
		return valid

def day7part2():
	#shamelessly stolen from reddit because fuck regexes
	lines = [re.split(r'\[([^\]]+)\]', line) for line in open('day7data.txt')]
	parts = [(' '.join(p[::2]), ' '.join(p[1::2])) for p in lines]
	print('Answer #2:', sum(any(a == c and a != b and b+a+b in hn for a, b, c in zip(sn, sn[1:], sn[2:])) for sn, hn in parts))