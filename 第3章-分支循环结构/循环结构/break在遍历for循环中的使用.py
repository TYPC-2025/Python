for i in 'hello':
    if i=='e':
        break
    print(i)

#用for循环模拟用户登录
for i in range(3):  #循环3次
    user_name=input('请输入用户名：')
    pwd=input('请输入密码：')
    if user_name=='ty' and pwd=='8888':
        print('系统正在登陆中，请稍后……')
        break
    else:
        if i<2:
            print('用户名或密码不正确，您还有',2-i,'次机会')
else:
    print('三次均输入错误！')