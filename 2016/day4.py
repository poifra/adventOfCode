import re
from collections import Counter

def cesar(message, n):
	'''
	cesar cipher
	'''
	message = message.replace('-',' ').upper()
	ALPHABET = "abcdefghijklmnopqrstuvwxyz".upper()
	SIZE = len(ALPHABET)
	res = ''
	print(message)
	for c in message:
		res += ' ' if c == ' ' else ALPHABET[(ALPHABET.find(c) + n) % SIZE]

	return res

def day4part1():
	with open('day4data.txt') as f:
		regex = r'([a-z-]+)(\d+)\[(\w+)\]'
		s = 0
		for code, roomid, checksum in re.findall(regex, f.read()):
			code = code.replace('-','')
			mostCommon = [(-n,c) for c,n in Counter(code).most_common()]
			sort = ''.join(c for n,c in sorted(mostCommon))
			if sort.startswith(checksum):
				s+=int(roomid)
		return s


def day4part2():
	with open('day4data.txt') as f:
		regex = r'([a-z-]+)(\d+)\[(\w+)\]'
		s = 0
		for code, roomid, checksum in re.findall(regex, f.read()):
			code = code.replace('-','')
			mostCommon = [(-n,c) for c,n in Counter(code).most_common()]
			sort = ''.join(c for n,c in sorted(mostCommon))
			if sort.startswith(checksum):
				roomid = int(roomid)
				decode = cesar(code,roomid)
				print(decode)
				if 'NORTH' in decode:
					s+=roomid
				
		return s
