for t in range(int(input())):
	R, P, D = map(int, input().split())
	I = [input().split() for _ in range(R)]
	w = next(float(w) for _,w,p in I if p=="100.0") * D / P
	print("Recipe", '#', t+1)
	for n,_,p in I:
		print(n, f"{w*float(p)/100:.1f}")
	print("----------------------------------------")