def valid(d):
	return 0<d<21 or d%2==0 and 0<d<41 or d%3==0 and 0<d<61

def output(*args):
	for d in args:
		if d%3 == 0:
			print("triple", d//3)
		elif d%2 == 0:
			print("double", d//2)
		else:
			print("single", d)
	exit()

n = int(input())
for d in range(1, min(n+1, 61)):
	if not valid(d):
		continue
	if d == n:
		output(d)
	for e in range(1, min(n-d+1, 61)):
		if not valid(e):
			continue
		if d+e == n:
			output(d, e)
		f = n-d-e
		if valid(f):
			output(d, e, f)
else:
	print("impossible")
