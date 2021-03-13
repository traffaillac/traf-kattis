N = int(input())
dom = {}
for _ in range(N):
	res = input()
	dom[res] = dom.get(res, 0) + 1
same = 0
for _ in range(N):
	res = input()
	if dom.get(res, 0) > 0:
		dom[res] -= 1
		same += 1
print(same)
