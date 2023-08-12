D = int(input())
R = int(input())
T = int(input())
for r in range(4, 45):
	t = r-D
	R0 = r*(r+1)//2-6
	T0 = max(t*(t+1)//2-3, 0)
	if R0+T0 == R+T:
		break
print(R-R0)
