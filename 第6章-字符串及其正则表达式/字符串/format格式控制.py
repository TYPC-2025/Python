#引导符，对齐符（引导符放在{}里面）
s='helloworld'
print('{0:*<20}'.format(s)) #字符串显示宽度为20，左对齐，空白部分用*填充
print('{0:*>20}'.format(s))
print('{0:*^20}'.format(s))

#居中对齐
print(s.center(20,'*'))
print('{0:*^20}'.format(s))

#千位分隔符（只适用于整数和浮点数）
print('{0:,}'.format(987654321))
print('{0:,}'.format(987654321.44791))

#浮点数小数部分的精度
print('{0:.2f}'.format(3.1415926))

#字符串类型，表示最大显示长度1
print('{0:.5}'.format('helloworld')) #hello

#整数类型进制
a=425
print('二进制:{0:b},十进制:{0:d},八进制:{0:o},十六进制:{0:x},十六进制:{0:X}'.format(a))

#浮点数类型进制
b=3.1415926
print('{0:.2f},{0:.2E},{0:.2e},{0:.2%}'.format(b))