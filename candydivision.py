from math import sqrt

N = int(input())
nums = []
for i in range(int(sqrt(N))):
	if N % (i+1) == 0:
		nums.append(i)
		nums.append(N // (i+1) - 1)
if nums[-1] == nums[-2]:
	nums.pop()
nums.sort()
print(" ".join(map(str, nums)))
