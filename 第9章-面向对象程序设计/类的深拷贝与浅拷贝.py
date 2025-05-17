class CPU:
    pass
class Disk:
    pass

class Computer():
    #计算机由CPU和Disk组成
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

#创建一个对象
cpu=CPU()
disk=Disk()
#创建一个计算机对象
com=Computer(cpu,disk)
#变量（对象）的赋值
com1=com # com1 和 com 指向同一个对象内存地址
print(com,'子对象的内存地址:',com.cpu,com.disk)
print(com1,'子对象的内存地址:',com1.cpu,com1.disk) #输出内存地址

print('-'*50)

#类对象的浅拷贝copy.copy()
# com 和 com2 是不同对象，但它们的 cpu 和 disk 是一样的（内存地址相同）
import copy
com2=copy.copy(com) #com2是新产生的对象，com2的子对象cpu,disk不变
print(com,'子对象的内存地址',com.cpu,com.disk)
print(com2,'子对象的内存地址:',com2.cpu,com2.disk)

print('-'*50)

#类对象的深拷贝copy.deepcopy()
import copy
com3=copy.deepcopy(com) #com3是新产生的对象，com3的子对象cpu,disk也会发生改变
print(com,'子对象的内存地址',com.cpu,com.disk)
print(com3,'子对象的内存地址:',com3.cpu,com3.disk)