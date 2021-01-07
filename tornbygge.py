input()
X = [int(i) for i in input().split()]
towers = 1
for i in range(len(X) - 1):
	if X[i+1] > X[i]:
		towers += 1
print(towers)
