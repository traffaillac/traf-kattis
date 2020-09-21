last = None
words = set()
for i in range(int(input())):
	w = input()
	if last and w[0] != last[-1] or w in words:
		print(f"Player {i%2+1} lost")
		break
	words.add(w)
	last = w
else:
	print("Fair Game")
