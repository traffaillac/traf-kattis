# from math import comb
from math import factorial
def comb(n, k):
	return factorial(n) // (factorial(k) * factorial(n-k))

for _ in range(int(input())):
	R, S, X, Y, W = map(int, input().split())
	p = (S-R+1)/S # probability of success for 1 dice
	win = sum(comb(Y,k) * p**k * (1-p)**(Y-k) for k in range(X, Y+1))
	print('yes' if win*W > 1 else 'no')
