N = [i+1 for i in range(26)] # number of letters to add to end with letter chr(i)
for c in input():
	i = ord(c) - 97
	N[i] = min((N[j]+i-j-1 for j in range(i)), default=0)
print(min(N[i]+25-i for i in range(26)))
