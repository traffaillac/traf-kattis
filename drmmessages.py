s = input()
a = [ord(c)-ord('A') for c in s[:len(s)//2]]
b = [ord(c)-ord('A') for c in s[len(s)//2:]]
ra, rb = sum(a), sum(b)
a = [(i+ra)%26 for i in a]
b = [(i+rb)%26 for i in b]
print(''.join(chr(ord('A')+(i+j)%26) for i,j in zip(a, b)))