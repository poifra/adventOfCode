day1=max([sum(map(int,x.split('\n'))) for x in open('input1.txt').read().split('\n\n')])
day1part2=sum(sorted([sum(map(int,x.split('\n'))) for x in open('input1.txt').read().split('\n\n')])[-3:])

day2=sum([{'AX':4,'AY':8,'AZ':3,'BX':1,'BY':5,'BZ':9,'CX':7,'CY':2,'CZ':6}[x] for x in open('input2.txt').read().replace(' ','').split('\n')])
day2part2=sum([{'AX':3,'AY':4,'AZ':8,'BX':1,'BY':5,'BZ':9,'CX':2,'CY':6,'CZ':7}[x] for x in open('input2.txt').read().replace(' ','').split('\n')])

day3=sum(map(lambda x: __import__('string').ascii_letters.index(x)+1,[[c for c in t[0] if c in t[1]][0] for t in [(l[0:int(len(l)/2)],l[int(len(l)/2):len(l)]) for l in open('input3.txt').read().split('\n')]]))
day3part2=sum(map(lambda x: __import__('string').ascii_letters.index(x)+1,[[c for c in t[0] if c in t[1] and c in t[2]][0] for t in [(l1.replace('\n',''),l2.replace('\n',''),l3.replace('\n','')) for l1,l2,l3 in __import__('itertools').zip_longest(*[open('input3.txt')]*3)]]))

day4=sum([1 if (t1<=t3 and t2>=t4) or (t1>=t3 and t2<=t4) else 0 for t1,t2,t3,t4 in [map(int,sum(tuple(map(lambda x:x.split('-'),l.split(','))),[])) for l in open('input4.txt').read().split('\n')]])
day4part2=sum([1 if (t1>=t3 and t1<=t4) or (t2>=t3 and t2<=t4) or (t1<=t3 and t2>=t3) or (t1<=t4 and t2>=t4) else 0 for t1,t2,t3,t4 in [map(int,sum(tuple(map(lambda x:x.split('-'),l.split(','))),[])) for l in open('input4.txt').read().split('\n')]])

lst = ['',deque('FTCLRPGQ'),deque('NQHWRFSJ'),deque('FBHWPMQ'),deque('VSTDF'),deque('QLDWVFZ'),deque('ZCLS'),deque('ZBMVDF'),deque('TJB'),deque('QNBGLSPH')]
for inst in [(x[0],x[1],x[2]) for x in [list(map(int,x.split(' '))) for x in open('input5.txt').read().replace('move ','').replace('from ','').replace('to ','').split('\n')]]:
    lst[inst[2]].extend(lst[inst[1]].pop() for x in range(inst[0]))
day5 = "".join([x.pop() for x in lst[1:]])

lst = ['',deque('FTCLRPGQ'),deque('NQHWRFSJ'),deque('FBHWPMQ'),deque('VSTDF'),deque('QLDWVFZ'),deque('ZCLS'),deque('ZBMVDF'),deque('TJB'),deque('QNBGLSPH')]
for inst in [(x[0],x[1],x[2]) for x in [list(map(int,x.split(' '))) for x in open('input5.txt').read().replace('move ','').replace('from ','').replace('to ','').split('\n')]]:
    lst[inst[2]].extend([lst[inst[1]].pop() for x in range(inst[0])][::-1])
day5part2 = "".join([x.pop() for x in lst[1:]])

day6 = [len(set(line[i:i+4]))==4 for line in open('input6.txt') for i in range(len(line))].index(True)+4
day6part2 = [len(set(line[i:i+14]))==14 for line in open('input6.txt') for i in range(len(line))].index(True)+14


