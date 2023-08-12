C = [ord(c)-ord('A') for c in input()]
K = [ord(k)-ord('A') for k in input()]
print(''.join(chr(ord('A')+(c+k if i&1 else c-k)%26) for i, (c, k) in enumerate(zip(C, K))))