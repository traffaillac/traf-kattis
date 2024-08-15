n = int(input())
S = sorted(((int(s), i+1) for i, s in enumerate(input().split())), reverse=True)
print("impossible" if S[0][0]*2>sum(s for s,i in S) else ' '.join(str(i) for s,i in S))