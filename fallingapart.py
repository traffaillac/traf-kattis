input()
A = [int(i) for i in input().split()]
A.sort(reverse=True)
print(
	sum(a for i, a in enumerate(A) if i%2==0),
	sum(a for i, a in enumerate(A) if i%2==1))
