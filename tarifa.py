X = int(input())
N = int(input())
rem = X
for n in range(N):
	rem += X - int(input())
print(rem)
