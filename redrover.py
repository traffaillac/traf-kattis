s = input()
m = len(s)
for i in range(len(s)-1):
	for j in range(i+2,len(s)+1):
		m = min(m, len(s)-s.count(s[i:j])*(j-i-1)+j-i)
print(m)