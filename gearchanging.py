N, M, P = map(int, input().split())
C = [int(c) for c in input().split()]
D = [int(d) for d in input().split()]
cadences = [c/d for c in C for d in D]
cadences.sort()
print('Ride on!' if all(cadences[i]*(1+P/100) >= cadences[i+1] for i in range(len(cadences)-1)) else 'Time to change gears!')
