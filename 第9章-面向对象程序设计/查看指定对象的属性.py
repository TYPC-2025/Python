class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f'大家好，我叫：{self.name},今年{self.age}岁了')

#创建Person类的对象
per=Person('ty',18)
print(dir(per)) #查看属性

print(per) #自动调用了__str__方法