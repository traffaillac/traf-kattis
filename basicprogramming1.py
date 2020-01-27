N, t = (int(i) for i in input().split())
A = [int(i) for i in input().split()]
if t == 1:
	print(7)
elif t == 2:
	print('Bigger' if A[0]>A[1] else 'Equal' if A[0]==A[1] else 'Smaller')
elif t == 3:
	print(max(min(A[0],A[1]), min(max(A[0],A[1]),A[2])))
elif t == 4:
	print(sum(A))
elif t == 5:
	print(sum(a for a in A if a%2==0))
elif t == 6:
	print(''.join(chr(97+a%26) for a in A))
elif t == 7:
	i = 0
	for j in range(200_000):
		i = A[i]
		if not 0<=i<N:
			print('Out')
			break
		if i==N-1:
			print('Done')
			break
	else:
		print('Cyclic')
