
def revertCaptcha(text, mode = 1):
	#mode is for part 1 or 2
	size = len(text)
	s = 0
	for i,n in enumerate(text):
		if mode == 1 and text[i] == text[(i+1)%size]:
			s += int(n)
		if mode == 2 and text[i] == text[(int(i+size/2)) % size]:
			s += int(n)
	return s


def problem():
	# problem description : http://adventofcode.com/2017/day/1
	#part 1
	assert revertCaptcha('1122') == 3
	assert revertCaptcha('1111') == 4
	assert revertCaptcha('1234') == 0
	assert revertCaptcha('91212129') == 9
	data = open('day1data.txt','r').read()
	print("part 1 :",revertCaptcha(data))

	#part 2
	assert revertCaptcha('1212',2) == 6
	assert revertCaptcha('1221',2) ==  0
	assert revertCaptcha('123123',2) == 12
	assert revertCaptcha('12131415',2) == 4
	print("part 2 :",revertCaptcha(data,2))


if __name__ == '__main__':
	problem()