# corner case: empty list at the end
from collections import deque

for _ in range(int(input())):
	prog = input()
	n = int(input())
	s = input()[1:-1]
	X = deque(map(int, s.split(",")) if s else [])
	rev = False
	try:
		for inst in prog:
			if inst == "R":
				rev = ~rev
			elif rev:
				X.pop()
			else:
				X.popleft()
		print("[" + ",".join(map(str, reversed(X) if rev else X)) + "]")
	except:
		print("error")