try:
    score=eval(input('请输入分数:'))
    if 0<=score<=100:
        print('分数:',score)
    else:
        raise Exception('分数不正确')
except Exception as e:
    print(e)