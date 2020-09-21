# 2 2 1 1
N = int(input())
arrows = [0]*1_000_001
count = 0
for h in [int(i) for i in input().split()]:
	if arrows[h] == 0:
		count += 1
	else:
		arrows[h] -= 1
	arrows[h-1] += 1
print(count)
