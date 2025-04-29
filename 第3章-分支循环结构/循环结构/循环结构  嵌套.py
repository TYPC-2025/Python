#输出长方形
for i in range(1,4):  #外层循环 行
    for j in range(1,5):  #内层循环 列
        print('*',end='')
    print() #空的print语句作用是 换行

#输出直角三角形
for i in range(1,6): #5行
    for j in range(1,i+1): #第1行打印一个*，第2行打印两个*，以此类推
        print('*',end='')
    print()    

#输出倒直角三角形
for i in range(1,6): #5行
    for j in range(1,7-i):
        print('*',end='')
    print()    

#输出金字塔三角形
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end='')
    for j in range(1,2*i):
        print('*',end='')
    print()        

#打印菱形

row=eval(input('请输入菱形的行数：'))
while row%2==0:
    print('重新输入菱形的行数：')
    row=eval(input('请输入菱形的行数：'))
#行数为奇数，输出菱形    
top_row=row//2+1
for i in range(1,top_row+1):
    for j in range(1,top_row+1-i):
        print(' ',end='')
    for j in range(1,2*i):
        print('*',end='')
    print()    
bottom_row=row//2
for i in range(1,bottom_row+1):
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(1,2*bottom_row-2*i+2):
        print('*',end='')
    print()    

#空心菱形
row=eval(input('请输入菱形的行数：'))
while row%2==0:
    print('重新输入菱形的行数：')
    row=eval(input('请输入菱形的行数：'))
#行数为奇数，输出菱形    
top_row=row//2+1
for i in range(1,top_row+1):
    for j in range(1,top_row+1-i):
        print(' ',end='')
    for k in range(1,2*i):
        if k==1 or k==2*i-1:
            print('*',end='')
        else:
            print(' ',end='')    
    print()    
bottom_row=row//2
for i in range(1,bottom_row+1):
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(1,2*bottom_row-2*i+2):
        if k==1 or k==2*bottom_row-2*i+2-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()    