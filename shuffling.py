from itertools import count
n,shuf = input().split()
n = int(n)
deck = orig = tuple(range(n))
for i in count(1):
	if shuf == 'out':
		deck = tuple(deck[i%2*((n+1)//2)+i//2] for i in range(n))
	else:
		deck = tuple(deck[(i+1)%2*(n//2)+i//2] for i in range(n))
	if deck == orig: break
print(i)