#父类（Person类）
class Person: #没有加小括号，默认继承了object
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(f'大家好，我叫:{self.name},我今年:{self.age}岁了')

#子类（Student）继承父类（Person）
class Student(Person):
    #编写初始化的方法
    def __init__(self, name, age,stuno):
        super().__init__(name, age) #调用父类的初始化方法
        self.stuno=stuno

#子类（Doctor）继承父类（Person）
class Doctor(Person):
    def __init__(self, name, age,department):
        super().__init__(name, age)
        self.department=department


#创建第一个子类对象
stu=Student('ty',18,2405030232)
stu.show()
#创建第二个子类对象
doctor=Doctor('fkf',30,'外科')
doctor.show()