moves = {'U': (0,-1), 'D': (0,1), 'L': (-1,0), 'R': (1,0)}
L, W = (int(i) for i in input().split())
lanes = []
for l in range(L):
	O, I, S = (int(i) for i in input().split())
	lanes.append([O, I, S, 1] if l%2==0 else [W-1-O, I, S, -1])
P, M = input().split()
x, y = int(P), L
squish = False
for m in M:
	x += moves[m][0]
	y += moves[m][1]
	for i, l in enumerate(lanes):
		if l[2] == 0 and i == y and abs(x-l[0])%l[1] == 0:
			print('squish')
			exit()
		for j in range(l[2]):
			l[0] += l[3]
			if i == y and abs(x-l[0])%l[1] == 0:
				print('squish')
				exit()
print('safe' if y<0 else 'squish')
