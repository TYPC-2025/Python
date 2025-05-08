d={1001:'李华',1002:'张三',1003:'王五'}
print(d)

#向字典中添加元素（直接赋值）
d[1004]='李四'
print(d)

#获取字典中所有的key
keys=d.keys()
print(keys)
print(list(keys))
print(tuple(keys))

#获取字典中所有的value
values=d.values()
print(values)
print(list(values))
print(tuple(values))

#如果将字典中的数据转成key-value的形式，以 元组 的方式进行展现
lst=list(d.items())
print(lst)

d=dict(lst)
print(d)  #转化成字典类型

#使用pop函数删除元素（先把值取出，再删除）
print(d.pop(1001))
print(d)

print(d.pop(1008,'不存在')) #删除一个本身不存在的值

#随机删除
print(d.popitem())
print(d)

#清空字典中的元素
d.clear()
print(d)

#python中一切对象均有布尔值
print(bool(d))  #空字典的布尔值为False
