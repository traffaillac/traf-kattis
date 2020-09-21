input()
ans = [input().split(", ") for _ in range(int(input()))]
def dist(a:list, b:list):
	return sum(i != j for i, j in zip(a, b))
def incongruousity(a:list):
	return max(dist(a, b) for b in ans if b != a)
i = min(incongruousity(a) for a in ans)
for a in ans:
	if incongruousity(a) == i:
		print(", ".join(a))
