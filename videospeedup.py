n, p, k = map(int, input().split())
total = 0.0
speed = 100
last = 0
for t in map(int, input().split()):
	total += (t - last) * speed / 100
	speed += p
	last = t
print(total + (k - last) * speed / 100)
