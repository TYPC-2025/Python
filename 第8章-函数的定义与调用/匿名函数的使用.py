"""只有一个函数体的函数"""

def calc(a,b):
    return a+b
print(calc(10,20))

print('-'*50)

"""使用匿名函数来简化上述函数"""

s=lambda a,b:a+b
print(type(s))  #<class 'function'>
#调用匿名函数
print(s(10,20))

print('-'*50)

"""进行列表取值的时候也能使用匿名函数"""
#列表的正常取值操作
lst=[10,20,30,40]
for i in range(len(lst)):
    print(lst[i])
print()

print('-'*50)

#使用匿名函数
for i in range(len(lst)):
    result=lambda x:x[i] #x是形式参数
    print(result(lst)) #lst是实际参数

print('-'*50)

"""对列表进行排序 也能使用匿名函数"""
student_scores=[
    {'name':'rt','score':98},
    {'name':'il','score':91},
    {'name':'nj','score':87},
    {'name':'gh','score':59}
]
#对列表进行排序，规则是字典中的  成绩
student_scores.sort(key=lambda x:x.get('score'),reverse=True) #降序
print(student_scores)