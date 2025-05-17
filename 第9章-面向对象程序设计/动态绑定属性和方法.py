class Student:
    #类属性：定义在类中，方法外的变量
    school='四川XXX教育'

    #初始化方法
    def __init__(self,xm,age):  #xm,age是方法的参数，是局部变量，xm，age的作用域是整个__init__方法
        self.name=xm #=左侧是  实例属性  ，xm是局部变量，将局部变量的值xm赋值给实例属性self.name
        self.age=age #实力的名称和局部变量的名称可以相同

    #定义在类中的函数，成为方法，自带一个参数self
    def show(self):  #实例方法
        print(f'我叫:{self.name},今年:{self.age}岁了')


#创建两个Student类型的对象
stu=Student('ty',18)
stu2=Student('tyc',17)
print(stu.name,stu.age)
print(stu2.name,stu2.age)

#为stu2动态绑定一个实例属性
stu2.gender='男'
print(stu2.name,stu2.age,stu2.gender)

#动态绑定方法（给某个对象临时添加一个方法）
def introduce():
    print('我是一个普通的函数，我被动绑定成了stu2对象的方法')
stu2.fun=introduce  #这是函数的一个赋值，不能加小括号，加了小括号就变成调用了
# fun就是stu2对象的方法
# 会将stu2.fun当作一个函数来调用
#实例方法（打点调用）
stu2.fun() # 绑定的是无参数的函数，调用时也不能带参数

"""如何绑定带self的函数"""
"""使用types.MethodType"""
import types

def speak(self):
    print(f'我是{self.name}，这是我动态绑定的方法')

stu2.speak = types.MethodType(speak, stu2)
stu2.speak()  # 输出：我是tyc，这是我动态绑定的方法
