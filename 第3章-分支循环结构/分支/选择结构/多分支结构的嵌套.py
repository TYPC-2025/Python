# 注意第二行没有使用eval函数，但第四行使用了eval函数
answer=input('请问你喝酒了吗？')
if answer=='喝了':
    proof=eval(input('请输入酒精含量：'))
    if proof<20:
        print('没有构成酒驾')
    elif proof<80:
        print('你酒驾了')
    else:
        print('你构成醉驾，请跟我们到警局一趟')
else:
    print('没什么事，你走吧！')        