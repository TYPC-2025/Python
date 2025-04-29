score=eval(input('请输入您的成绩：'))
if score<0 or score>100:
    print('成绩有误！')
elif 90<=score<=100:
    print('4.0')
elif 85<=score<90:
    print('3.7')
elif 82<=score<85:
    print('3.3')
elif 78<=score<=81:
    print('3.0')
else:
    print('绩点小于3.0')