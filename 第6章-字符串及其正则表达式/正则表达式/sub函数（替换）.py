import re
pattern='黑客|破解|反爬'
s='我想学习python，像破解一些VIP视频，Python可以实现无底线反爬吗？'
new_s=re.sub(pattern,'XXX',s)  #'XXX'代表违禁词的显示方式
print(new_s)
