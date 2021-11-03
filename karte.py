S = input()
i = 0
suits = {'P':set(), 'K':set(), 'H':set(), 'T':set()}
while i < len(S):
	T = S[i]
	XY = int(S[i+1:i+3])
	if XY in suits[T]:
		print('GRESKA')
		break
	suits[T].add(XY)
	i += 3
else:
	print(' '.join(str(13-len(s)) for s in suits.values()))
