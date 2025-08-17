#（1）import直接导入的形式
import my_info
print(my_info.name)
my_info.info()

#（1）import直接导入的形式，创建一个别名
import my_info as a
print(a.name)
a.info()

#（2）from……import
from my_info import name #导入的是一个具体的变量的名称
print(name)
#info() #报错

from my_info import info#导入的是一个具体的函数的名称
info()


#（3）通配符
from my_info import *
print(name)
info()

#同时导入多个模块（用英文逗号隔开）
import math,time,random