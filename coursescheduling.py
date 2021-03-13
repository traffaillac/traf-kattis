n = int(input())
courses = {}
for _ in range(n):
	student, course = input().rsplit(' ', 1)
	courses.setdefault(course, set()).add(student)
for course, students in sorted(courses.items()):
	print(course, len(students))
