I = {'b':'$', 'j':'*', 't':'|'}
for _ in range(int(input())):
	S = []
	for a in input().replace('.',''):
		if a in "$|*":
			S.append(a)
		elif not S or S.pop()!=I[a]:
			print("NO")
			break
	else:
		print("NO" if S else "YES")