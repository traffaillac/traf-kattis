trips = {}
for _ in range(int(input())):
	s, y = input().split()
	trips.setdefault(s, []).append(int(y))
for years in trips.values():
	years.sort()
for _ in range(int(input())):
	s, k = input().split()
	print(trips[s][int(k)-1])
