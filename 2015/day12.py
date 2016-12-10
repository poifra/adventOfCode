import json #fun times
import sys
NUMBERS = []
def jsonSum(data, ignoreRed = False):
	global NUMBERS
	if type(data) is list:
		for elem in data:
			if type(elem) is dict and ignoreRed and "red" in elem.values():
				return
			jsonSum(elem)
	elif type(data) is dict:
		if ignoreRed:
			if("red" not in data.values()):
				for elem in data.keys():
					jsonSum(data[elem])
		else:
			for elem in data.keys():
				jsonSum(data[elem])
	elif type(data) is str:
		return
	else: #its an int
		NUMBERS.append(data)
		return
	
if __name__ == '__main__':
	with open(sys.argv[1], 'r') as file:
		jsonData = json.load(file)
		jsonSum(jsonData)
	#	print("part 1", sum(NUMBERS))
	#	global NUMBERS
	#	NUMBERS = []
		jsonSum(jsonData,True)
		print("part 2", sum(NUMBERS))