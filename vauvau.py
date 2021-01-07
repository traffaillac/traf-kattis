A, B, C, D = map(int, input().split())
P, M, G = (int(i)-1 for i in input().split())
p = (P % (A + B) < A) + (P % (C + D) < C)
m = (M % (A + B) < A) + (M % (C + D) < C)
g = (G % (A + B) < A) + (G % (C + D) < C)
nums = ['none', 'one', 'both']
print(nums[p])
print(nums[m])
print(nums[g])
