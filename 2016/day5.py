import hashlib
import random
import string 
import sys
INPUT = 'ojvtpuvg'
def day5part1():
	n = 0
	pwd = ''
	while len(pwd) != 8:
		guess = (INPUT+str(n)).encode('utf-8')
		m = hashlib.md5()
		m.update(guess)
		checksum = m.hexdigest()
		if checksum.startswith('00000'):
			print(n,checksum)
			pwd += checksum[5]
		n += 1
	return pwd

def day5part2():
	n = 0
	pwd = list('$$$$$$$$')
	while '$' in pwd:
		guess = (INPUT+str(n)).encode('utf-8')
		m = hashlib.md5()
		m.update(guess)
		checksum = m.hexdigest()
		if checksum.startswith('00000'):
			pos = int(checksum[5],16)
			char = checksum[6]
			if pos < len(pwd) and pwd[pos] == '$':
				pwd[pos] = char
		n += 1

		#extra cool hacking effect
		if n%10000 == 0:
			hack = []
			for c in pwd:
				if c == '$':
					hack.append(str(random.choice(string.ascii_letters+string.punctuation+string.digits))[-1])
				else:
					hack.append(c)
			sys.stdout.write("password: {} \r".format("".join(hack)))
			sys.stdout.flush()
	print('\n')
	return "".join(pwd)