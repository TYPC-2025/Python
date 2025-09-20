import socket
#（1）创建socket对象
socket_obj=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#（2）绑定主机和IP端口
socket_obj.bind(('127.0.0.1',8888))

#（3）使用listen()进行监听
socket_obj.listen(5)

#（4）等待客户端的连接
client_socket,cilent_addr=socket_obj.accept()

#（5）接收来自客户端的数据
info=client_socket.recv(1024).decode('utf-8')  #while循环  info是初始化变量
while info !='bye':                         #条件判断
    if info !='':
        print('接收到的数据是',info)
    #准备发送的数据
    data=input('请输入要发送的数据:')

    #服务器端回复客户端
    client_socket.send(data.encode('utf-8'))
    if data=='bye':
        break                              #17行到25行是循环
    info=client_socket.recv(1024).decode('utf-8')   #改变变量


#关闭socket对象
client_socket.close() #关闭客户端的
socket_obj.close() #关闭服务器端的