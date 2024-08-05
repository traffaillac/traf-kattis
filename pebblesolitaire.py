from functools import cache

@cache
def left(B):
	n = B.count('o')
	for i in range(10):
		if B[i:i+3]=="-oo":
			n = min(n, left(B[:i]+"o--"+B[i+3:]))
		elif B[i:i+3]=="oo-":
			n = min(n, left(B[:i]+"--o"+B[i+3:]))
	return n

for _ in range(int(input())):
	print(left(input()))