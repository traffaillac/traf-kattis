# apr18, jun20, aug22, oct24, dec26, feb29
y = int(input())
jan = (y-2018)*12-3
print("yes" if jan%26>=15 else "no")
