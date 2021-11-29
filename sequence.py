N = int(input())
print(N.bit_length())
print(' '.join(map(str, (1 << i for i in range(N.bit_length())))))
