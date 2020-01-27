s = input()
b = sum(map(lambda c: 1 if c == 'B' else 0, s))
w = sum(map(lambda c: 1 if c == 'W' else 0, s))
print(1 if b == w else 0)
