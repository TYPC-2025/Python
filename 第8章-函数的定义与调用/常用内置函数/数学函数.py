print('绝对值:',abs(100),abs(-100),abs(0))
print('商和余数:',divmod(13,4))
print('最大值:',max('hello'))
print('最大值:',max([10,30,45,6]))
print('最小值:',min('hello'))
print('最小值:',min([10,30,45,6]))
print('求和:',sum([12,54,23]))  #直接使用函数
print('x的y次幂:',pow(2,3))

#四舍五入
print(round(3.1415926))  #只有一个参数，即保留整数

print(round(3.1415926,3))  #保留三位小数

print(round(314.15926,-1))  #310.0

print(round(314.15926,-2))  #300.0