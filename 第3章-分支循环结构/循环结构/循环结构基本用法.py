# 遍历字符串
for i in 'hello':
    print(i)

# range函数
for i in range(1,11):
    print(i)

#对循环变量更进一步的操作
for i in range(1,11):
    #print(i)
    if i%2==0:
        print(i,'是偶数')

#计算一到十之间的累加和     
s=0   
for i in range(1,11):
    s+=i
    
    print('一到十之间的累加和：',s)


#100-999之间的水仙花数
for i in range(100,1000):
    gw=i%10
    sw=i//10%10
    bw=i//100
    if gw**3+sw**3+bw**3==i:
        print(i)

#for……else……结构
s=0   
for i in range(1,11):
    s+=i
else:    
    print('一到十之间的累加和：',s)

#无限循环while的使用
answer=input('今天要上课吗？')
while answer=='y':
    print('一定要好好听课，争取高绩点')
    answer=input('今天要上课吗？')

#用while无限循环语句计算1-100之间的累加和
s=0
i=1
while i<=100:
    s+=i
    i+=1

print('1-100之间的累加和:',s)
#该代码和下面这种写法输出结果是一样的
s=0
i=1
while i<=100:
    s+=i
    i+=1
else:
    print('1-100之间的累加和:',s)
