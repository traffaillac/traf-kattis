from collections import deque

steps = {0b01100_00000_10000_11000_11110_11111: 0}
fifo = deque()
fifo.append(0b01100_00000_10000_11000_11110_11111)

def down(s:int, conf:int, pos:int, bit:int, diff:int):
	new = conf & ~(bit >> diff) | conf << diff & bit | pos - diff << 25
	if not new in steps:
		steps[new] = s
		fifo.append(new)

def up(s:int, conf:int, pos:int, bit:int, diff:int):
	new = conf & ~(bit << diff) | conf >> diff & bit | pos + diff << 25
	if not new in steps:
		steps[new] = s
		fifo.append(new)

while steps[fifo[0]] < 10:
	conf = fifo.popleft()
	s = steps[conf] + 1
	pos = conf >> 25
	conf &= 0x1ffffff
	bit = 1 << pos
	i = pos // 5
	j = pos % 5
	if i >= 2 and j >= 1:
		down(s, conf, pos, bit, 11)
	if i >= 2 and j < 4:
		down(s, conf, pos, bit, 9)
	if i >= 1 and j >= 2:
		down(s, conf, pos, bit, 7)
	if i >= 1 and j < 3:
		down(s, conf, pos, bit, 3)
	if i < 4 and j >= 2:
		up(s, conf, pos, bit, 3)
	if i < 4 and j < 3:
		up(s, conf, pos, bit, 7)
	if i < 3 and j >= 1:
		up(s, conf, pos, bit, 9)
	if i < 3 and j < 4:
		up(s, conf, pos, bit, 11)

N = int(input())
for n in range(N):
	conf = 0
	for i in range(5):
		for j, c in enumerate(input()):
			if c == '1':
				conf |= 1 << (i * 5 + j)
			elif c == ' ':
				conf |= (i * 5 + j) << 25
	if conf in steps:
		print('Solvable in %d move(s).'%steps[conf])
	else:
		print('Unsolvable in less than 11 move(s).')
