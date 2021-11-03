# 1 1 2 3 1
# 1 1 2 3 5 8 0 8
# 1 1 2 3 5 8 13 21 12 11 1 12
for q in range(int(input())):
	k = int(input())
	first = [-1] * k
	cur, last = 2 % k, 1
	n = 2
	while first[cur] < 0:
		first[cur] = n
		cur, last = (cur + last) % k, cur
		n += 1
	print(first[cur])
