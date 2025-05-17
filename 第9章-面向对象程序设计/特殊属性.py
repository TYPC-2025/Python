class A(object):
    pass
class B(object):
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
#创建类的对象
a=A()
b=B()
#创建C类的对象
c=C('ty',18)

#查看对象的的属性
print('对象a的属性字典:',a.__dict__) # 对象的属性字典
print('对象b的属性字典:',b.__dict__)
print('对象c的属性字典:',c.__dict__)

print('对象a所属的类:',a.__class__)
print('对象b所属的类:',b.__class__)
print('对象c所属的类:',c.__class__)

print('A类的父类元组:',A.__bases__)
print('B类的父类元组:',B.__bases__)
print('C类的父类元组:',C.__bases__)

print('A类的父类:',A.__base__)
print('B类的父类:',B.__base__)
print('C类的父类:',C.__base__) #如果继承了很多个父类，只显示第一个父类；如果继承了FatherA,FatherB的方法，在FatherA和FatherB当中有同名的方法，在调用时，默认调用第一个父类的方法

print('A类的层次结构:',A.__mro__)
print('B类的层次结构:',B.__mro__)
print('C类的层次结构:',C.__mro__) #首先继承了A类，B类，又间接继承了object类

print('A类的子类列表:',A.__subclasses__())
print('B类的子类列表:',B.__subclasses__())
print('C类的子类列表:',C.__subclasses__())