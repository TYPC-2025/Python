import pandas as pd
import matplotlib.pyplot as plt
#读取excel文件
df=pd.read_excel('JD手机销售数据.xlsx')
print(df)
#解决中文乱码
plt.rcParams['font.sans-serif']=['SimHei'] #字体

#开始绘图，设置画布的大小
plt.figure(figsize=(5,4))
labels=df['商品名称']
y=df['北京出库销量']
print(labels)
print(y)

#开始绘制饼图
plt.pie(y,labels=labels,autopct='%1.1f%%',startangle=90) #角度90°，饼状图从最上面开始区分

#设置x,y轴
plt.axis('equal')
plt.title('2025年北京各手机品牌出库量占比图')

#显示饼状图
plt.show()
