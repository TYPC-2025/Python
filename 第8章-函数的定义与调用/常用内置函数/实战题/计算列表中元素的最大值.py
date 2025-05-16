"""编写函数实现计算列表中元素的最大值"""
import random
def get_max(lst):
    x=lst[0]
    for i in range(1,len(lst)):
        if lst[i]>x:
            x=lst[i]
    return x
   
#调用
lst=[random.randint(1,100) for item in range(10)]
print(lst)

#计算元素的最大值
max=get_max(lst)
print(max)