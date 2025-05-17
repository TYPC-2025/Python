class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #方法重写
    def __str__(self):
        return '这是一个人类，具有name和age两个实例属性'

#创建Person类的对象
per=Person('ty',18)
print(per) #输出__str__方法中的内容，直接输出对象名，实际调用__str__方法
#下面这种写法输出和上面是相同的
print(per.__str__()) #手动调用