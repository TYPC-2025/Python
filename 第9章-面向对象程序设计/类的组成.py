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

    #静态方法
    # 静态方法 不接收 self 或 cls 参数，跟类和对象都没直接关系。
    #
    # 主要是写在类中、但与类无关的功能代码。
    @staticmethod
    def sm():
        print('这是一个静态方法，不能调用实例属性，也不能调用实例方法')
    # 调用实例属性：print(self.name)  报错
    # 调用实例方法：print.show()  报错

    #类方法
    # 可以访问或修改类属性（如 cls.school）
    #
    # 不能访问实例属性和实例方法（因为没有 self）
    @classmethod
    def cm(cls):
        print('这是一个类方法，不能调用实例属性，也不能调用实例方法')
    # 调用实例属性：print(self.name)  报错
    # 调用实例方法：print.show()  报错


"""创建类的对象"""
stu=Student('ty',18)
"""实例属性，使用 对象名 进行打点调用"""
print(stu.name,stu.age)
"""类属性，直接使用 类名 打点调用"""
print(Student.school)
"""实例方法，使用 对象名 进行打点调用"""
stu.show()
"""类方法，@classmethod进行修饰的方法，直接使用 类名 打点调用"""
Student.cm()

"""静态方法，@staticmethod进行修饰都方法，直接使用 类名 打点调用"""
Student.sm()