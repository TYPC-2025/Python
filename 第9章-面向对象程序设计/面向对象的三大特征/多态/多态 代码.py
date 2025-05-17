class Person():
    def eat(self):
        print('人喜欢吃五谷杂粮')

class Cat():
    def eat(self):
        print('猫喜欢吃鱼')

class Dog():
    def eat(self):
        print('狗喜欢啃骨头')

#这三个类中都有一个同名的方法，eat
#编写函数
def fun(obj):
    obj.eat() #通过调用obj（对象）调用eat方法

#创建三个类的对象
per=Person()
cat=Cat()
dog=Dog()

#调用fun函数
fun(per)
fun(cat)
fun(dog)