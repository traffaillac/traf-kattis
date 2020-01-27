list1 = [None] * 5000
list2 = [None] * 5000
list3 = [0] * 5000
while True:
	N = int(input())
	if N == 0:
		break
	list1 = [(int(input()), n) for n in range(N)]
	list2 = [int(input()) for n in range(N)]
	list1.sort()
	list2.sort()
	for n in range(N):
		list3[list1[n][1]] = list2[n]
	for n in range(N):
		print(list3[n])
	print()