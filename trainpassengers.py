C,n = (int(i) for i in input().split())
c = 0
for _ in range(n):
	left,enter,wait = (int(i) for i in input().split())
	if left>c or c-left+enter>C or wait>0 and c-left+enter<C:
		print('impossible')
		exit()
	c += enter-left
print('possible' if c==0 else 'impossible')