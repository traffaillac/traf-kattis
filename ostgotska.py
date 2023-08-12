W = input().split()
print("dae ae ju traeligt va" if sum('ae' in w for w in W)*100>=40*len(W) else "haer talar vi rikssvenska")