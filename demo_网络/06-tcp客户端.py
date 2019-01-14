import socket


def main():
    # 1. 创建tcp的套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 链接服务器
    tcp_socket.connect(("192.168.1.103", 8080))

    # 3. 给服务器发送消息
    send_data = input("请输入你要发送的消息: ")
    tcp_socket.send(send_data.encode("utf-8"))

    # 接收服务端消息
    recv_data = tcp_socket.recv(1024)
    print("服务端发送的消息: %s" % recv_data.decode("utf-8"))

    # 4. 关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()
