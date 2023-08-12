S = int(input())
print(f"{S}:")
for l in range(S-1, 1, -1):
	q, r = divmod(S, l)
	if r==0 or r==(l+1)//2:
		print(f"{q+(r>0)},{q}")
