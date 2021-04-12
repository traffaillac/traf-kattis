l, w = map(int, input().split())
if w<l or w>26*l:
	print('impossible')
	exit()
while l > 0:
	i = min(w - (l-1), 26)
	print(chr(96 + i), end="")
	w -= i
	l -= 1
print()
