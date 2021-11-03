fingers = {
	'c': (2, 3, 4, 7, 8, 9, 10),
	'd': (2, 3, 4, 7, 8, 9),
	'e': (2, 3, 4, 7, 8),
	'f': (2, 3, 4, 7),
	'g': (2, 3, 4),
	'a': (2, 3),
	'b': (2,),
	'C': (3,),
	'D': (1, 2, 3, 4, 7, 8, 9),
	'E': (1, 2, 3, 4, 7, 8),
	'F': (1, 2, 3, 4, 7),
	'G': (1, 2, 3, 4),
	'A': (1, 2, 3),
	'B': (1, 2)}
for _ in range(int(input())):
	pressed = [False] * 10
	presses = [0] * 10
	for note in input():
		for f in range(10):
			if f+1 in fingers[note]:
				if not pressed[f]:
					presses[f] += 1
				pressed[f] = True
			else:
				pressed[f] = False
	print(' '.join(map(str, presses)))
