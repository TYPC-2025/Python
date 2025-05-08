"""创建字典"""
#（1）直接用{}来创建
d={10:'cat',20:'dog',30:'epr',20:'zoo'}
print(d)  #当key相同时，value值进行了覆盖

#（2）zip函数
lst1=[10,20,30,40]
lst2=['cat','dog','pet','zoo','car']
zipobj=zip(lst1,lst2)
print(zipobj)  #无法看到元素
print(list(zipobj)) #转化成列表类型进行查看

#转成字典
lst3=[10,20,30,40]
lst4=['cat','dog','pet','zoo','car']
zipobj=zip(lst3,lst4)
print(zipobj)  #无法看到元素
d=dict(zipobj)  #使用dict函数
print(d)

#（3）使用参数创建字典
d=dict(cat=10,dog=20)
print(d)

t=(10,20,30)
print({t,10}) #元组可以作为字典中的key
#列表是不能作为字典中的键的

#字典属于序列
print('max:',max(d))
print('min:',min(d))
print('len:',len(d))

#字典的删除
del d
print(d)
