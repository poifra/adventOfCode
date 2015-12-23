import sys

def bestCombo(ing, calCount = False):
	'''
	brute force that shit
	'''
	maxValue = -1
	for i in range(100):
		for j in range(100-i):
			for k in range(100-i-j):
			
				l = 100-i-j-k #all that remains, no need a loop
				totalCap = ing[0]['capacity']*i+j*ing[1]['capacity']+k*ing[2]['capacity']+l*ing[3]['capacity']
				totalDur = ing[0]['durability']*i+j*ing[1]['durability']+k*ing[2]['durability']+l*ing[3]['durability']
				totalFla = ing[0]['flavor']*i+j*ing[1]['flavor']+k*ing[2]['flavor']+l*ing[3]['flavor']
				totalTex = ing[0]['texture']*i+j*ing[1]['texture']+k*ing[2]['texture']+l*ing[3]['texture']
				totalCal = ing[0]['calories']*i+j*ing[1]['calories']+k*ing[2]['calories']+l*ing[3]['calories']
				
				if totalCap <= 0 or totalDur <= 0 or totalFla <= 0 or totalTex <=0:
					score = 0
				else:
					score = totalCap*totalDur*totalFla*totalTex

				if calCount and totalCal != 500:
					continue
				if score > maxValue:
					maxValue = score
	return maxValue

if __name__ == '__main__':
	with open(sys.argv[1], 'r') as file:
		content = file.read().replace(',','').replace(':','').split('\n')
		ings = []
		for line in content:
			name,_,capacity,_,durability,_,flavor,_,texture,_,calories = line.split(' ')
			ing = dict()
			ing['name'] = name
			ing['capacity'] = int(capacity)
			ing['durability'] = int(durability)
			ing['flavor'] = int(flavor)
			ing['texture'] = int(texture)
			ing['calories'] = int(calories)
			ings.append(ing)
		print("part1", bestCombo(ings))
		print("part2", bestCombo(ings,True))