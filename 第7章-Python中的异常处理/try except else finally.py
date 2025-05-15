#try-except结构

try:
    num1=int(input('请输入一个整数:'))
    num2=int(input('请输入一个整数:'))
    result = num1 / num2 
    print('结果:',result)
except ZeroDivisionError:
    print('除数不能为0') 
except ValueError:
    print('不能将字符串转化为整数')
except BaseException:
    print('未知异常')

#try……except……else
try:
    num1=int(input('请输入一个整数:'))
    num2=int(input('请输入一个整数:'))
    result = num1 / num2 
except ZeroDivisionError:
    print('除数不能为0') 
except ValueError:
    print('不能将字符串转化为整数')
except BaseException:
    print('未知异常')
else:
    print('结果:',result)

#try……except……else……finally
try:
    num1=int(input('请输入一个整数:'))
    num2=int(input('请输入一个整数:'))
    result = num1 / num2 
except ZeroDivisionError:
    print('除数不能为0') 
except ValueError:
    print('不能将字符串转化为整数')
except BaseException:
    print('未知异常')
else:
    print('结果:',result)
finally:
    print('程序执行结束！')  #无论程序是否有异常都要执行