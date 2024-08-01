K, a, b = map(int, open(0))
C = [(i, (K-a*i)//b) for i in range(K//a+1) if (K-a*i)%b==0]
print(len(C))
print('\n'.join(f"{i} {j}" for i, j in C))