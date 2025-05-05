"""列表的遍历操作"""

lst=['hello','world','python','html']
#使用遍历循环for遍历列表元素
for item in lst:
    print(item)
#使用for循环，range()函数，len()函数，根据索引进行遍历
for i in range(0,len(lst)):
    print(i,'-->',lst[i])
#使用enumearte函数
for index,item in enumerate(lst):
    print(index,item) #index是序号，不是索引

for index,item in enumerate(lst,start=1):#手动修改序号的起始值
    print(index,item) #index是序号，不是索引


for index,item in enumerate(lst,1):#手动修改序号的起始值
    print(index,item) #index是序号，不是索引

"""列表的相关操作(元素变化但是内存地址不变)"""
lst=['hello','world','python']
print('原列表：',lst,id(lst))
#增加元素的操作
lst.append('html')
print('增加元素之后：',lst,id(lst))

#使用insert(index,x)在指定的index位置插入元素x
lst.insert(1,3.84)
print(lst)

#列表元素的删除操作
lst.remove('hello')
print('删除元素之后的列表：',lst,id(lst))


#使用pop(index)根据 索引 将元素取出，然后再删除
print(lst.pop(2))
print(lst)

#列表的逆向输出（不会产生新的列表，在原列表的基础上进行的）
lst.reverse()
print(lst)

#列表的拷贝，将产生一个新的列表对象
new_lst=lst.copy()
print(lst,id(lst))
print(new_lst,id(new_lst))

#列表元素的修改（根据索引修改）
lst[1]='winner'
print(lst)

#清除列表中所有元素clear()
lst.clear()
print(lst,id(lst))