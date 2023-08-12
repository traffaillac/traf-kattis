n, m = map(int, input().split())
a = [-1]*(m-n) + [ord(c)-ord('a') for c in input()]
b = [ord(c)-ord('a') for c in input()]
k = [-1]*m
for i in range(m-1, n-1, -1):
	k[i] = (b[i]-a[i])%26
	a[i-n] = k[i]
print(''.join(chr(ord('a')+c) for c in a))
