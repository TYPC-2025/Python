from socket import socket,AF_INET,SOCK_STREAM
#从socket模块中导入socket类
#AF_INET 用于Internet之间的进程通信
#SOCK_STREAM  表示使用 TCP 编程

#（1）创建socket对象
server_socket=socket(AF_INET,SOCK_STREAM)

#（2）绑定IP地址和端口
ip='127.0.0.1'
port=8888 #不要和系统的一些端口一样，比如MYSQL端口是3306
server_socket.bind((ip,port)) #里面是元组类型

#（3）使用listen()进行监听
server_socket.listen(5)
print('服务器已经启动')

#（4）等待客户端的连接
client_socket,client_addr=server_socket.accept() #系列解包赋值

#（5）接收来自客户端的数据
data=client_socket.recv(1024) #1024个数据
print('客户端发过来的数据为:',data.decode('utf-8')) #要求客户端发过来的数据都是使用utf-8进行编码的

#（6）关闭socket
server_socket.close()