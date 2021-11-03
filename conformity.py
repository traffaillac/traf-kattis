popularity = {}
for i in range(int(input())):
	courses = tuple(sorted(map(int, input().split())))
	popularity[courses] = popularity.get(courses, 0) + 1
best = max(popularity.values())
print(sum(p for p in popularity.values() if p == best))
