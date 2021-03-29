X = input()
digits = ''.join(sorted(X))
for x in range(int(X)+1, 10**len(X)):
	if ''.join(sorted(str(x))) == digits:
		print(x)
		break
else:
	print(0)
