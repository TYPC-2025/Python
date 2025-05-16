#（1）bool
print('非空字符串的布尔值:',bool('hello'))
print('空字符串的布尔值:',bool(''))  #是空字符串不是空格字符串
print('空列表的布尔值:',bool([]))
print('空列表的布尔值:',bool(list()))
print('空元组的布尔值:',bool(()))
print('空元组的布尔值:',bool(tuple()))
print('空集合的布尔值:',bool(set()))
print('空字典的布尔值:',bool({}))
print('空字典的布尔值:',bool(dict()))

print('-'*50)

print('非0数值型的布尔值:',bool(123))
print('整数0的布尔值:',bool(0))
print('浮点数0.0的布尔值:',bool(0.0))

print('-'*50)

#（2）str
lst=[10,20,30]
print(type(lst),lst)

s=str(lst)
print(type(s),s)

#（3）int
print('-'*30,'float str类型转化成int类型','-'*30)

print(int(90.4)+int('30'))

#注意：下面情况会报错
# print(int('96.3'))
# print(int('a'))

#（4）float
print('-'*30,'int str类型转化成float类型','-'*30)

print(float(90)+float('96.2'))

#（5）list
s='hello'
print(list(s))

#（6）tuple set
seq=range(1,10)
print(tuple(seq))
print(set(seq))
print(list(seq))
