for i in range(50):
	N = int(input())
	if N == 0: break
	if i > 0: print()
	stack1, stack2 = 0, 0
	for _ in range(N):
		action, m = input().split()
		m = int(m)
		if action == "DROP":
			print("DROP 1", m)
			stack1 += m
		elif action == "TAKE":
			if stack2 > 0:
				take = min(stack2, m)
				print("TAKE 2", take)
				stack2 -= take
				m -= take
			if m > 0:
				print("MOVE 1->2", stack1)
				print("TAKE 2", m)
				stack1, stack2 = 0, stack1 - m
