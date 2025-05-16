"""不带返回值的函数"""
def calc(a,b):
    print(a+b)
calc(10,20)
# 下面实际上是打印函数的返回值
print(calc(1,2)) #无返回值，输出None

print("-"*50)

"""带返回值的函数（只有一个返回值）"""
def calc2(a,b):
    s=a+b
    return s

get_s=calc2(1,2)  #存储到变量中
print(get_s)  #3

#计算1+2+3
get_s2=calc2(calc2(1,2),3)
print(get_s2)


"""带返回值的函数（有多个返回值）"""
def get_sum(num):
    s=0
    odd_sum=0
    even_sum=0
    for i in range(1,num+1):
        if i%2!=0:
            odd_sum+=i
        else:
            even_sum+=i
        s+=i
    return odd_sum,even_sum,s
#调用
result=get_sum(10)
print(type(result))  #tuple
print(result)
#要将元组的内容全部提取出来（解包赋值）
a,b,c=get_sum(10)
print(a)
print(b)
print(c)