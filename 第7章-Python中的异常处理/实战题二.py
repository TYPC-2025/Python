try:
    a=int(input('请输入第一条边长:'))
    b=int(input('请输入第二条边长:'))
    c=int(input('请输入第三条边长:'))
    if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
        print('第一条边长:',a)
        print('第二条边长:',b)
        print('第三条边长:',c)
    else:
        raise Exception(a,b,c,'不能构成三角形')  #最终得到元组
except Exception as e:
    print(e)


try:
    a=int(input('请输入第一条边长:'))
    b=int(input('请输入第二条边长:'))
    c=int(input('请输入第三条边长:'))
    if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
        print('第一条边长:',a)
        print('第二条边长:',b)
        print('第三条边长:',c)
    else:
        raise Exception(f'{a},{b},{c},不能构成三角形')  #最终得到字符串
except Exception as e:
    print(e)



try:
    a=int(input('请输入第一条边长:'))
    b=int(input('请输入第二条边长:'))
    c=int(input('请输入第三条边长:'))
    if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
        print(f'三角形的边长为:{a},{b},{c}')    #最终排版更好看
    else:
        raise Exception(a,b,c,'不能构成三角形')  #最终得到元组
except Exception as e:
    print(e)