n = int(input())
print(' '*(n+1)+'x')
for i in range(n):
	print(' '*(n-i)+'/'+' '*(1+2*i)+'\\')
print('x'+' '*(1+n*2)+'x')
for i in range(n):
	print(' '*(1+i)+'\\'+' '*(n*2-i*2-1)+'/')
print(' '*(n+1)+'x')