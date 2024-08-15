S = " abcdefghijklmnopqrstuvwxyz"
for _ in range(int(input())):
	l = input()
	if l[0]=='e':
		u = 0
		for s in l[2:]:
			u = (S.find(s)+u)%27
			print(S[u], end='')
		print()
	else:
		print(''.join(S[(S.find(b)-S.find(a))%27] for a, b in zip(l[1:], l[2:])))