class Student:
    def __init__(self,name,gender):
        self.name=name
        self.__gender=gender  #私有的实例属性（在类外部无法直接访问）

    #使用 @property 修改方法，将方法转成属性使用
    # 它的作用是将方法 gender 转换为属性，使得你可以通过 stu.gender
    # 的方式访问它，而不需要显式调用方法 stu.gender()
    @property
    def gender(self): # 属性访问器
        return self.__gender # 返回学生的性别
    
stu=Student('tyc','男')
print(stu.name,'的性别是：',stu.gender)  #stu.gender会直接执行stu.gender()

