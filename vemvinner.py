G = (input()+input()+input()).replace(' ','')
for i, j, k in ((0,1,2),(3,4,5),(6,7,8),(0,4,8),(2,4,6),(0,3,6),(1,4,7),(2,5,8)):
    if G[i]==G[j]==G[k]!='_':
        print("Johan" if G[i]=='X' else "Abdullah", "har vunnit")
        exit()
print("ingen har vunnit")