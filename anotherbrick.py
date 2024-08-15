h, w, _ = map(int, input().split())
r = w
for x in map(int, input().split()):
	r -= x
	if r<0:
		print("NO")
		exit()
	elif r==0:
		r = w
		h -= 1
		if h==0:
			print("YES")
			exit()