class Student():
    #首尾双下划线
    def __init__(self,name,age,gender):
        self._name=name #self._name受保护的，只能本类和子类访问
        self.__age=age #self.__age表示私有的，只能类本身去访问
        self.gender=gender #普通的示例操作，类的内部，外部及子类都可以访问

    def _fun1(self): # 受保护的
        print('子类及本身都能访问')

    def __fun2(self): # 私有的
        print('只有定义的类可以访问') # 外部不能直接访问

    def show(self): # 普通的实例方法
        self._fun1() # 类本身访问受保护的方法
        self.__fun2() # 类本身访问私有方法
        print(self._name) #受保护的实例属性
        print(self.__age) #私有的实例属性
#创建一个学生类的对象
stu=Student('ty',18,'女')

#在类的外部
print(stu._name)
# print(stu.__age) #报错

#调用受保护的实例方法
stu._fun1() #子类及本身都可以访问
#访问私有方法
# stu.__fun2() #报错，因为没在定义的类里

"""访问私有的实例属性和方法 需要用以下方法"""
print(stu._Student__age)
stu._Student__fun2()

print(dir(stu)) #可以展示这个对象中所有的属性和方法