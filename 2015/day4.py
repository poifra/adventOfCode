def magicNumber(input,n):
	from hashlib import md5
	for i in range(10000000): 
		if(md5((input+str(i)).encode()).hexdigest()[:n] == '0'*n): return i

if(__name__=="__main__"):
	input = "bgvyzdsv"
	print(magicNumber(input,5))
	print(magicNumber(input,6))