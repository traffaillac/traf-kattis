n, p = map(int, input().split())
P = "mfewmnumber ofcamount of.mostmfewestcleast.moremfewerclessmmanycmuchclittle"
N = dict(input().split() for _ in range(n))
for _ in range(p):
	a, b = input().rsplit(' ',1)
	print(["Not on my watch!","Correct!"][P[P.find(a)-1]!=N[b]])