password, string = input().split()
pos = 0
for i, c in enumerate(string):
	idx = password.find(c, pos)
	if idx == pos:
		pos += 1
	elif idx > pos:
		print("FAIL")
		break
else:
	print("PASS" if pos == len(password) else "FAIL")
