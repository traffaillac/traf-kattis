from collections import *
print(sum(n%2 for n in Counter(input()).values())-1)