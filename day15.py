import sys

def bestCombo(ingredients):
	#brute force that shit
	maxValue = -100000000000
	for i in range(100):
		for j in range(100):
			for k in range(100):
				for l in range(100):
					if i+j+k+l <= 100:
						score = 0
						for ing in ingredients:
						if score > maxValue:
							maxValue = score
	return score

if __name__ == '__main__':
	with open(sys.argv[1], 'r') as file:
		content = file.read().replace(',','').replace(':','').split('\n')
		ingredients = []
		for line in content:
			name,_,capacity,_,durability,_,flavor,_,texture,_,calories = line.split(' ')
			ing = dict()
			ing['name'] = name
			ing['capacity'] = int(capacity)
			ing['durability'] = int(durability)
			ing['flavor'] = int(flavor)
			ing['texture'] = int(texture)
			ing['calories'] = int(calories)
			ingredients.append(ing)
		print(bestCombo(ingredients)