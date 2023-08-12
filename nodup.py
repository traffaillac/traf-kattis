from collections import Counter
print("yes" if set(Counter(input().split()).values()) == {1} else "no")