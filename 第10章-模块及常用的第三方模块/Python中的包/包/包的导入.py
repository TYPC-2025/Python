# (1) 会输出__init__文件中的代码
import admin.my_admin as a #包名(admin).模块名(my_admin)
a.info()

#(2)
from admin import my_admin as b #from 包名 import 模块 as 别名
b.info()

#(3)
from admin.my_admin import info #from 包名，模块名 import 函数、变量
info()

print('-'*50)

#(4)
from admin.my_admin import *
print(name)