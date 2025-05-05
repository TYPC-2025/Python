s={10,20,30}

#向集合中添加元素
s.add(40)
print(s)

#从集合中删除元素
s.remove(20)
print(s)

#清空集合中所有元素
s.clear()
print(s)

"""集合的遍历操作"""
#for遍历
s={10,20,30}
for item in s:
    print(item)

#使用enumerate函数遍历
for index,item in enumerate(s,1):
    print(index,'--->',item)