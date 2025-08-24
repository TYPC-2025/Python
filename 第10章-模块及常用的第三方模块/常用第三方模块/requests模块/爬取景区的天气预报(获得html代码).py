import requests
url='https://www.weather.com.cn/weather1d/101010100.shtml' #爬虫打开浏览器上的网址
resp=requests.get(url)  #打开浏览器并打开网址
resp.encoding='utf-8' #设置编码格式
print(resp.text) #resp响应对象  对象名。属性名  resp.text