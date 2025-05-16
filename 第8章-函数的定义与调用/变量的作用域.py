"""局部变量"""
def calc(a,b):
    s=a+b
    return s
# print(a,b,s)  #报错，a,b是函数的参数，参数是局部变量；s是函数中定义的变量，也是局部变量


"""全局变量"""
a=100 #全局变量
def calc(x,y):
    return a+x+y
print(a)
print(calc(10,20))
    
print('-'*50)

def calc2(x,y):
    a=200  #局部变量
    return a+x+y
print(calc2(10,20))
print(a) # 输出的是全局变量的值

print('-'*50)

def calc3(x,y):
    global s1  #使用了global关键字，s就变成了全局变量
    s1=300  #声明和赋值必须  分开执行
    return s1+x+y
print(calc3(10,20))
print(s1)
    