I=input
P=I()+I()+I()+I()
s=0
for i,c in enumerate(P):
	if c!='.':
		j=ord(c)-65
		s+=abs(i//4-j//4)+abs(i%4-j%4)
print(s)