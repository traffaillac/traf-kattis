from collections import deque

def main():
	final = 0b11111111_10101010_01010101_00000000
	init = 0
	for r in range(4):
		for c, g in enumerate(input()):
			init |= "RGBY".index(g) << (r * 8 + c * 2)
	if init == final:
		return print(0)
	dist = {init: 0, final: -1}
	fifo = deque((init, final))
	while True:
		state = fifo.popleft()
		new = dist[state]
		new += -1 if new < 0 else 1
		neighbours = (
			state&0xffffff00 | state<<2&0x000000fc | state>>6&0x00000003,
			state&0xffff00ff | state<<2&0x0000fc00 | state>>6&0x00000300,
			state&0xff00ffff | state<<2&0x00fc0000 | state>>6&0x00030000,
			state&0x00ffffff | state<<2&0xfc000000 | state>>6&0x03000000,
			state&0xffffff00 | state>>2&0x0000003f | state<<6&0x000000c0,
			state&0xffff00ff | state>>2&0x00003f00 | state<<6&0x0000c000,
			state&0xff00ffff | state>>2&0x003f0000 | state<<6&0x00c00000,
			state&0x00ffffff | state>>2&0x3f000000 | state<<6&0xc0000000,
			state&0xfcfcfcfc | state<<8&0x03030300 | state>>24&0x00000003,
			state&0xf3f3f3f3 | state<<8&0x0c0c0c00 | state>>24&0x0000000c,
			state&0xcfcfcfcf | state<<8&0x30303000 | state>>24&0x00000030,
			state&0x3f3f3f3f | state<<8&0xc0c0c000 | state>>24&0x000000c0,
			state&0xfcfcfcfc | state>>8&0x00030303 | state<<24&0x03000000,
			state&0xf3f3f3f3 | state>>8&0x000c0c0c | state<<24&0x0c000000,
			state&0xcfcfcfcf | state>>8&0x00303030 | state<<24&0x30000000,
			state&0x3f3f3f3f | state>>8&0x00c0c0c0 | state<<24&0xc0000000)
		for n in neighbours:
			old = dist.get(n)
			if old == None:
				dist[n] = new
				fifo.append(n)
			elif old < 0 <= new or new < 0 <= old:
				return print(abs(new - old) - 1)

main()
