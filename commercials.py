P = int(input().split()[1])
current_sum, best_sum = 0, 0
for studs in map(int, input().split()):
	current_sum = max(0, current_sum + studs - P)
	best_sum = max(best_sum, current_sum)
print(best_sum)
