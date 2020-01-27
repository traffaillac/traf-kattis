while True:
	try:
		domain = {k:0 for k in input().split()[1:]}
		codomain = {k:0 for k in input().split()[1:]}
	except: break
	for x, _, y in set(tuple(input().split()) for n in range(int(input()))):
		domain[x] += 1
		codomain[y] += 1
	print('not a function' if any(v>1 for v in domain.values()) else
		'bijective' if all(v==1 for v in codomain.values()) else
		'surjective' if all(v>=1 for v in codomain.values()) else
		'injective' if all(v<=1 for v in codomain.values()) else
		'neither injective nor surjective')
