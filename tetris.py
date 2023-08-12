pieces = (
	((), (0, 0, 0)),
	((0,),),
	((0,1), (-1,)),
	((-1,-1), (1,)),
	((0,0), (1,), (-1,0), (-1,)),
	((0,0), (0,), (1,1), (-2,)),
	((0,0), (2,), (0,-1), (0,)))
C, P = map(int, input().split())
H = list(map(int, input().split()))
print(sum(all(H[i+1+j]==H[i]+h for j,h in enumerate(p)) for p in pieces[P-1] for i in range(C-len(p))))