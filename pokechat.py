S = input()
L = input()
print(''.join(S[int(L[i:i+3])-1] for i in range(0, len(L), 3)))
