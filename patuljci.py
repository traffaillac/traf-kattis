D = [int(input()) for _ in range(9)]
s = sum(D)-100
a, b = next((a, b) for a in D for b in D if a!=b and a+b==s)
for d in D:
	if d!=a and d!=b:
		print(d)