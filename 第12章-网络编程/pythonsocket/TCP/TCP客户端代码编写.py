import socket
#（1）创建socket对象
client_socket=socket.socket()

#（2）IP地址和主机端口（服务器）,向服务器端发动连接请求
ip='127.0.0.1'
port=8888  #必须与服务器上的是一样的
client_socket.connect((ip,port))
print('---------与服务器连接建立成功-------------')


#（3）发送数据
client_socket.send('welcome to China'.encode('utf-8'))

#（4）关闭
client_socket.close()
print('发送完毕')