from datetime import datetime

dt=datetime.now()
print('当前的系统时间为:',dt)

#datetime是一个类，也可以手动创建这个类的对象
dt2=datetime(2028,6,20,15,56)
print('dt2的数据类型:',type(dt2),'dt2表示的时间日期:',dt2)
print('年:',dt2.year,'月:',dt2.month,'日:',dt2.day)
print('时:',dt2.hour,'分:',dt2.minute,'秒:',dt2.second)

#比较两个datetime类型对象的大小
labor_day=datetime(2025,5,1,0,0,0)
national_day=datetime(2025,10,1,0,0,0)
print('劳动节比国庆节要早吗？',labor_day<national_day) #True

#datetime类型也能与字符串进行转换
nowdt=datetime.now()
nowdt_str=nowdt.strftime('%Y/%m/%d %H:%M:%S')
print('nowdt的数据类型是:',type(nowdt),'nowdt所表示的数据是:',nowdt)
print('nowdt_str的数据类型是:',type(nowdt_str),'nowdt_str所表示的数据是:',nowdt_str)

#字符串类型转成datetime类型
str_datetime='2025年10月1日 10点10分'
dt3=datetime.strptime(str_datetime,'%Y年%m月%d日 %H点%M分')
print('str_datetime的数据类型:',type(str_datetime),'str_datetime所表示的数据:',str_datetime)
print('dt3的数据类型:',type(dt3),'dt3所表示的数据:',dt3)