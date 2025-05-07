"""使用小括号来创建元组"""
t=('hello',[10,20,30],'Python','world')
print(t)

"""使用内置函数tuple()创建元组"""
t=tuple('helloworld')
print(t)

t=tuple([10,20,30,40])
print(t)

print('10在元组中是否存在：',(10 in t))
print('10在元组中不存在：',(10 not in t))
print('最大值：',max(t))
print('最小值：',min(t))
print('len:',len(t))
print('t.index:',t.index(10))
print('t.count:',t.count(10))

#如果元组中只有一个元素
t=(10)
print(t,type(t))  #输出的不是元组类型

#若要输出元组类型，逗号一定不能省略
t=(10,)
print(t,type(t))

#元组的删除（使用del）
del t
print(t)