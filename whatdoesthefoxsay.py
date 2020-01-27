from collections import OrderedDict

for t in range(int(input())):
	words = input().split()
	while True:
		animal, *sound = input().split()
		if animal == 'what':
			break
		for s in sound:
			words = list(filter(lambda w: w != s, words))
	print(' '.join(words))
