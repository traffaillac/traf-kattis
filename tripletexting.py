from statistics import median

s = input()
n = len(s)//3
print(''.join(median([s[i],s[n+i],s[n*2+i]]) for i in range(n)))
	