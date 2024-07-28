N = [input() for _ in range(int(input()))] + ['']
A = [a for a, b in zip(N, N[1:]) if a!="Present!" and b!="Present!"]
print('\n'.join(A) if A else "No Absences")