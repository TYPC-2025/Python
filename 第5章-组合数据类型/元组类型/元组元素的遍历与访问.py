t=('python','hello','world')
#根据索引访问元组
print(t[0])

#元组也支持切片操作
t2=t[0:3:2]
print(t2)

#元组的遍历(第一种)
for item in t:
    print(item)

#for+range()+len()(第二种)
for i in range(len(t)):
    print(i,t[i])

#使用enumerate函数
for index,item in enumerate(t):
    print(index,'-->',item)

for index,item in enumerate(t,start=1):
    print(index,'-->',item)
