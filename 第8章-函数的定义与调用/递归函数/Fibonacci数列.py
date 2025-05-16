def fac(n):
    if n==1 or n==2:
        return 1
    else:
        return fac(n-1)+fac(n-2)
    
print(fac(1))
print(fac(2))
print(fac(6)) #8
print(fac(9)) #34

#将1-9位上的数字都打印出来
for i in range(1,10):
    print(fac(i),end='\t') #'\t'是为了不换行
print()
