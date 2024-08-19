h=lambda n:n+h([n//2,n*3+1][n%2])if n-1 else 1
print(h(int(input())))