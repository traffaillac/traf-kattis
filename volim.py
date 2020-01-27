K = int(input()) - 1
N = int(input())
t = 0
for n in range(N):
	T, Z = input().split()
	t += int(T)
	if t > 210:
		print(K + 1)
		break
	if Z == 'T':
		K = (K + 1) % 8
