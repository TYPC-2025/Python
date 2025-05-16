"""个数可变的位置参数"""
def fun(*para):
    print(type(para))  #tuple
    for item in para:
        print(item)

#调用
fun(10,20,30,40)
fun(10)
fun(20,30)   #上面表示传入参数的个数不同
fun([10,20,30,40]) #列表只作为一整个元素参数
#要将列表中的所有元素单独列出来，应该在调用时，在参数前加一颗星，则能将列表进行解包
fun(*[10,20,30,40])


"""个数可变的关键字传参"""
def fun2(**kwpara):
    print(type(kwpara))  #dict
    for key,value in kwpara.items():
        print(key,'--->',value)

#调用
fun2(name='ty',age='18',height='170')  #关键字参数（采用赋值方式进行传参）

#不能直接将字典传进去

# d={'name':'ty','age':18,'height':170}
# fun2(d)

#如果参数是一个字典，前面必须加上  两颗星（进行系列解包操作）
d={'name':'ty','age':18,'height':160}
fun2(**d)