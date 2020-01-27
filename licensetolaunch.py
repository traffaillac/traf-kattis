input()
junk = [int(i) for i in input().split()]
print(min(range(len(junk)), key=junk.__getitem__))