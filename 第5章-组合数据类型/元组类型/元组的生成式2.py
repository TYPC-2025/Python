#使用__next__来依次输出元素
t=(i for i in range(1,4))
print(t)
print(t.__next__())
print(t.__next__())
print(t.__next__())
t=tuple(t)
print(t)    #已经用__next__方法将生成器中的所有元素全部取出来了，则最终结果应该是空（）