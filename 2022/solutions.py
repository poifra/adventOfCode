day1=max([sum(map(int,x.split('\n'))) for x in open('input1.txt').read().split('\n\n')])
day1part2=sum(sorted([sum(map(int,x.split('\n'))) for x in open('input1.txt').read().split('\n\n')])[-3:])

day2=sum([{'AX':4,'AY':8,'AZ':3,'BX':1,'BY':5,'BZ':9,'CX':7,'CY':2,'CZ':6}[x] for x in open('input2.txt').read().replace(' ','').split('\n')])
day2part2=sum([{'AX':3,'AY':4,'AZ':8,'BX':1,'BY':5,'BZ':9,'CX':2,'CY':6,'CZ':7}[x] for x in open('input2.txt').read().replace(' ','').split('\n')])

day3=sum(map(lambda x: __import__('string').ascii_letters.index(x)+1,[[c for c in t[0] if c in t[1]][0] for t in [(l[0:int(len(l)/2)],l[int(len(l)/2):len(l)]) for l in open('input3.txt').read().split('\n')]]))
day3part2=sum(map(lambda x: __import__('string').ascii_letters.index(x)+1,[[c for c in t[0] if c in t[1] and c in t[2]][0] for t in [(l1.replace('\n',''),l2.replace('\n',''),l3.replace('\n','')) for l1,l2,l3 in __import__('itertools').zip_longest(*[open('input3.txt')]*3)]]))