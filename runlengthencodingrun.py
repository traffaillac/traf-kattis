mode, S = input().split()
res = []
if mode == 'E':
    pos = 0
    while pos < len(S):
        end = pos + 1
        while end < len(S) and S[end] == S[pos]:
            end += 1
        res.append(S[pos])
        res.append(str(end - pos))
        pos = end
else:
    for c, d in zip(S[::2], S[1::2]):
        res += c * int(d)
print("".join(res))