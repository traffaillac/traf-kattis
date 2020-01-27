monster = input()
mech = []
i = 0
while i<len(monster):
	c = monster[i:i+3]
	if i<len(monster)-2 and (c=='RBL' or c=='RLB' or c=='BRL' or c=='BLR' or c=='LRB' or c=='LBR'):
		mech.append('C')
		i += 3
	else:
		mech.append('S' if monster[i]=='R' else 'K' if monster[i]=='B' else 'H')
		i += 1
print(''.join(mech))
