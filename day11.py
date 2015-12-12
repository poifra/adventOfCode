def isValid(password, isDigits = False):
	'''
	Checks if password is valid, given requirements
	'''
	if(len(password) != 8):
		return False
	
	if isDigits:
		password = "".join([chr(n) for n in password])
	
	if('i' in password or 'o' in password or 'l' in password):
		return False

	increasingSeq = False
	for c in range(len(password)-2):
		if(ord(password[c+2]) - 2 == ord(password[c]) and ord(password[c+1])-1 == ord(password[c])):
			increasingSeq = True
			break

	if not increasingSeq:
		return False

	subSeq1 = ""
	bothFound = False
	firstFound = False
	for c in range(len(password)-1):
		if password[c] == password[c+1] and not firstFound:
			subSeq1 = password[c]+password[c+1]
			firstFound = True
		if password[c] == password[c+1] and password[c]+password[c+1] != subSeq1 and firstFound: #eww
			bothFound = True
			break
	if not bothFound:
		return False

	return True

def newPassword(toChange):
	''' finds next valid password '''
	oldPass = [ord(c) for c in toChange] #easier to manipulate numbers
	lastChar = len(oldPass) - 1
	while not isValid(oldPass,True):
		if oldPass[lastChar] < 122:
			oldPass[lastChar] += 1
		else:
			shift = 0
			if oldPass[lastChar] == 122:
				oldPass[lastChar] += 1
			while oldPass[lastChar-shift] > 122:
				oldPass[lastChar-shift] = 97
				shift += 1
				oldPass[lastChar-shift] += 1
	reformed = "".join([chr(n) for n in oldPass])
	return reformed
	

if __name__ == '__main__':
	#isValid tests
	assert not isValid('hijklmmn')
	assert not isValid('abbceffg')
	assert not isValid('abbcegjk')
	assert isValid('abcdffaa')
	assert isValid('ghjaabcc')
	
	#newPassword tests
	assert newPassword('abcdefgh') == 'abcdffaa'
	assert newPassword('ghijklmn') == 'ghjaabcc'
	#prints solutions
	print("part 1",newPassword('hepxcrrq'))
	print("part 2",newPassword('hepxxzaa'))
	