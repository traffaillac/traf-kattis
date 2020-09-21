from sys import stdin
for i, words in enumerate(stdin.read().split("\n\n")):
	if i > 0: print()
	dyst = sorted(w[::-1] for w in words.split())
	cols = max(len(w) for w in dyst)
	for w in dyst:
		print(f"{w[::-1]:>{cols}}")
