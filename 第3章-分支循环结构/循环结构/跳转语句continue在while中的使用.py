#1-100之间的偶数累加和
s=0
i=1
while i<=100:
    if i%2==1:
        i+=1
        continue
    s+=i
    i+=1
print('1-100之间的偶数之和：',s)

#continue在for循环中的使用
s=0
for i in range(1,101):
    if i%2==1:
        continue
    s+=i
print('1-100之间的偶数之和：',s)