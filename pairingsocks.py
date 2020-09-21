n = int(input())
stack = []
for a in map(int, input().split()):
	if stack and a == stack[-1]:
		stack.pop()
	else:
		stack.append(a)
print("impossible" if stack else n*2)
