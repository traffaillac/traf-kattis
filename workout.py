# Jim using machine before other first usage
# Jim usage shorter than other recovery
# Jim starting at the middle of other recovery
jim = [int(i) for i in input().split()]
machines = [[int(i) for i in input().split()] for _ in range(10)]
time = 0
for _ in range(3):
	for i,m in enumerate(machines):
		u,r,t = m
		if time < t:
			m[2] = max(t, time+jim[i*2])
			time += jim[i*2] + jim[i*2+1]
		else:
			other_start = t+(time-t)//(u+r)*(u+r)
			jim_start = max(other_start+u, time)
			jim_end = jim_start+jim[i*2]
			m[2] = max(other_start+u+r, jim_end)
			time = jim_end + jim[i*2+1]
print(time-jim[-1])