N = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
S = [{N[(i+j)%12] for j in (0,2,4,5,7,9,11)} for i in range(12)]
input()
s = set(input().split())
print(' '.join(N[i] for i in range(12) if s<=S[i]) or "none")