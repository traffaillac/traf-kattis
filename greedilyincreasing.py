N = int(input())
A = [int(i) for i in input().split()]
gis = [A[0]]
largest = A[0]
for a in A:
	if a > largest:
		gis.append(a)
		largest = a
print(len(gis))
print(' '.join(map(str, gis)))
