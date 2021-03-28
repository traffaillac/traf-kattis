from collections import deque

for _ in range(int(input())):
	n = int(input())
	deck = deque()
	while n > 0:
		deck.appendleft(n)
		deck.rotate(n)
		n -= 1
	print(" ".join(map(str, deck)))
