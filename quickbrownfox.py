from string import ascii_lowercase

for _ in range(int(input())):
	missing = set(ascii_lowercase) - set(input().lower())
	print("pangram" if len(missing)==0 else "missing "+"".join(sorted(missing)))
