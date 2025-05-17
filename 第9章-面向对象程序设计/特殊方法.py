a=10
b=20

# 列出a这个对象的所有可用方法
print(dir(a)) #Python中一切皆对象
#加法
print(a+b)
print(a.__add__(b))
#减法
print(a-b)
print(a.__sub__(b))
#乘除法
print(a.__mul__(b))
print(a.__truediv__(b))
#不等号
print(f'{a}<{b}吗？',a.__lt__(b)) # less than
print(f'{a}<={b}吗？',a.__le__(b))
print(f'{a}=={b}吗？',a.__eq__(b))

print('-'*50)

print(f'{a}>{b}吗？',a.__gt__(b)) # greater than
print(f'{a}>={b}吗？',a.__ge__(b))
print(f'{a}!={b}吗？',a.__ne__(b)) # not equal

print('-'*50)

print(a.__mod__(b)) #取余
print(a.__floordiv__(b)) #整除
print(a.__pow__(2)) #幂