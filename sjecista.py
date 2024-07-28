I=0
for N in range(2,int(input())-1):
	for m in range(1,N):I+=m*(N-m)
print(I)