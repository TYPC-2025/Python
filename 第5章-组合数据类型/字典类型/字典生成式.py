import random
d={item:random.randint(1,100) for item in range(4)}
print(d)

#使用zip映射
lst=[1001,1002,1003]
lst2=['张三','李四','王五']
d={key:value for key,value in zip(lst,lst2)}
print(d)