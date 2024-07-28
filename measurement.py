U = "thou th inch in foot ft yard yd chain ch furlong fur mile mi league lea".split()
C = [1000, 12, 3, 22, 10, 8, 3]
v, s, _, t = input().split()
v = int(v)
i, j = U.index(s)//2, U.index(t)//2
while i<j:v/ = C[i];i+ = 1
while i>j:i- = 1;v* = C[i]
print(v)