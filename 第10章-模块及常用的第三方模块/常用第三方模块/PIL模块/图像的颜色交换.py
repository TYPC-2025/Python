from PIL import Image

#加载图片
im=Image.open('微信图片_20241231185134.jpg')
# print(type(im),im) #得到mode=RGB

#提取RGB图像的颜色通道，返回结果是图像的副本（系列解包赋值）
r,g,b=im.split()
print(r)
print(g)
print(b)

#合并通道
om=Image.merge(mode='RGB',bands=(g,b,r))
om.save('new_微信图片_20241231185134.jpg')