s = input()
for v in "aeiou":
	s = s.replace(v+'p'+v, v)
print(s)