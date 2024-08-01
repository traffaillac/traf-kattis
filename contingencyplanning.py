n = int(input())
if n>11:
	print("JUST RUN!!")
	exit()
s = 0
p = 1
for z in range(n,0,-1):
	p *= z
	s += p
print(s)