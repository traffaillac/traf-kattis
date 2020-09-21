# 10 1000
N = input()
k = len(input()) - 1
if k >= len(N):
	print('0.' + '0'*(k-len(N)) + N.rstrip('0'))
else:
	right = N[len(N)-k:].rstrip('0')
	print(N[:len(N)-k] + ('.' if len(right)>0 else '') + right)
