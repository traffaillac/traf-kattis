N = int(input())
x = int(input())
y = int(input())
L = sorted(map(int, input().split()))
s = 0
i = 0
while i < N and s+L[i]*x<=y*(i+1):
	s += L[i]*x
	i += 1
print(i)