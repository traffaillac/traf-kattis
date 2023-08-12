input()
s = input()
print(sum(a=='1' or b=='1' or c=='1' for a, b, c in zip(s, '0'+s, '00'+s)))