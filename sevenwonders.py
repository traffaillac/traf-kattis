from collections import Counter
s = input()
t, c, g = s.count('T'), s.count('C'), s.count('G')
print(t**2 + c**2 + g**2 + min(t, c, g)*7)