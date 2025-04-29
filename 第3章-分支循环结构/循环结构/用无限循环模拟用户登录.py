i=0
while i<3:
    user_name=input('请输入用户名：')
    pwd=input('请输入密码：')
    if user_name=='ty' and pwd=='8888':
        print('系统正在登录，请稍后')
        i=8 #任取一个大于3的数
    else:
        if i<2:
            print('用户名或密码不正确，您还有',2-i,'次机会')
        i+=1   
if i==3:
    print('三次均输入错误，设备已锁定') 