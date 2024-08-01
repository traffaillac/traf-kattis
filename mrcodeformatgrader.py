C, N = map(int, input().split())
L = list(map(int, input().split()))
Li = [0]+[i for i in range(1,N) if L[i]!=L[i-1]+1]+[N]
Lc = [f"{L[i]}-{L[j-1]}" if j-i>1 else str(L[i]) for i, j in zip(Li,Li[1:])]
print("Errors:", Lc[0] if len(Lc)==1 else ", ".join(Lc[:-1])+" and "+Lc[-1])
M = list({*range(1,C+1)}-{*L})
Mi = [0]+[i for i in range(1,C-N) if M[i]!=M[i-1]+1]+[C-N]
Mc = [f"{M[i]}-{M[j-1]}" if j-i>1 else str(M[i]) for i, j in zip(Mi,Mi[1:])]
print("Correct:", Mc[0] if len(Mc)==1 else ", ".join(Mc[:-1])+" and "+Mc[-1])
