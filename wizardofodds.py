N, K = map(int, input().split())
print('Your wish is granted!' if (N - 1).bit_length() <= K else 'You will become a flying monkey!')
