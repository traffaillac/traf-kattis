n = int(input())
tl, tr, bl, br = -2000000, -2000000, -2000000, -2000000
for _ in range(n):
	x, y = map(int, input().split())
	tl = max(tl, -x-y)
	tr = max(tr, x-y)
	bl = max(bl, -x+y)
	br = max(br, x+y)
print(4 if tl==-br and tr==-bl else tl+tr+bl+br+5 if tl==-br or tr==-bl else tl+tr+bl+br+4)
