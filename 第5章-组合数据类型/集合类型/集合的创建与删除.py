#用{}直接创建集合
s={10,20,30,40}
print(s)

#集合中只能存储不可变数据类型
#下面这种情况是错误的
"""
s={[10,20],[30,40]}
print(s)

"""

#使用set()函数来创建集合
s=set()
print(s) #输出空集合

s={}
print(s,type(s)) #输出的是字典，不是集合

s=set('helloworld')
print(s)  #集合是无序，不重复的

s1=set([10,20,30])  #列表
print(s1)

s2=set(range(1,10)) #range
print(s2)

#集合属于序列中的一种
print('max:',max(s2))
print('min:',min(s2))
print('9在集合中存在吗？',(9 in s2))
print('9在集合中不存在吗？',(9 not in s2))

#集合的删除操作（仍然使用 del 进行删除操作）
