"""可以同时使用位置传参和关键字传参"""
"""位置参数在前，关键字参数在后"""
def happy_birthday(name,age):
    print('祝'+name+'生日快乐')
    print(str(age)+'生日快乐')

happy_birthday('ty',age=18)