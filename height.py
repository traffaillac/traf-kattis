for _ in range(int(input())):
	K, *U = map(int, input().split())
	steps = 0
	O = [U.pop(0)]
	while U:
		h = U.pop(0)
		i = next((i for i, o in enumerate(O) if o>h), len(O))
		steps += len(O)-i
		O.insert(i, h)
	print(K, steps)
