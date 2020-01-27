input()
teas = [int(i) for i in input().split()]
input()
toppings = [int(i) for i in input().split()]
cheapest = min(p+toppings[int(t)-1] for p in teas for t in input().split()[1:])
print(max(int(input())//cheapest-1, 0))
