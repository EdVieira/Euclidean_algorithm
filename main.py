import sys

def division(x, y):
	return x / y, x % y

def euclides(l):
	l.sort()
	l.reverse()
	x, y = l[0],l[1]
	while division(x, y)[1] != 0:
		x1 = y
		y = division(x,y)[1]
		x = x1
	return y
res = []

l = sys.argv[1:]
if len(l)>1:
	l1 =[]
	for k in l:
		l1.append(int(k))
	res.append(euclides(l1))	
	for i in res:
		print i

"""
Enter a number list after the file name
$python main.py 365 900
5
"""