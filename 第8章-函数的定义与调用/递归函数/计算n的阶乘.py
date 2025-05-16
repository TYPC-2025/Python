def fac(n):  #计算n的阶乘
    if n==1:
        return 1
    else:
        return n*fac(n-1)
    
print(fac(5))
print(fac(10))
print(fac(3))