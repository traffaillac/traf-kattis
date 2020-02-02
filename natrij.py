h0,m0,s0 = (int(i) for i in input().split(':'))
h1,m1,s1 = (int(i) for i in input().split(':'))
time = (h1*3600+m1*60+s1 - h0*3600-m0*60-s0 - 1) % 86400 + 1
print(f"{time//3600:02}:{time//60%60:02}:{time%60:02}")
