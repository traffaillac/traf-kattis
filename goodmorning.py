valid = [
	True, True, True, True, True, True, True, True, True, True,
	True, True, True, True, True, True, True, True, True, True,
	True, False, True, True, False, True, True, False, True, True,
	False, False, False, True, False, False, True, False, False, True,
	True, False, False, False, True, True, True, True, True, True,
	True, False, False, False, False, True, True, False, True, True,
	False, False, False, False, False, False, True, False, False, True,
	True, False, False, False, False, False, False, True, True, True,
	True, False, False, False, False, False, False, False, True, True,
	False, False, False, False, False, False, False, False, False, True,
	
	True, False, False, False, False, False, False, False, False, False,
	True, True, True, True, True, True, True, True, True, True,
	True, False, True, True, False, True, True, False, True, True,
	False, False, False, True, False, False, True, False, False, True,
	True, False, False, False, True, True, True, True, True, True,
	True, False, False, False, False, True, True, False, True, True,
	False, False, False, False, False, False, True, False, False, True,
	True, False, False, False, False, False, False, True, True, True,
	True, False, False, False, False, False, False, False, True, True,
	False, False, False, False, False, False, False, False, False, True,
	
	True]

for _ in range(int(input())):
	k = int(input())
	for dk in range(200):
		if valid[k+dk]:
			print(k+dk)
			break
		if valid[k-dk]:
			print(k-dk)
			break
