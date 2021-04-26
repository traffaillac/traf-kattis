from collections import deque

pw = deque()
cur = 0
for c in input():
	if c == 'L':
		pw.rotate(1)
		cur -= 1
	elif c == 'R':
		pw.rotate(-1)
		cur += 1
	elif c == 'B':
		pw.pop()
		cur -= 1
	else:
		pw.append(c)
		cur += 1
pw.rotate(cur)
print(''.join(pw))
