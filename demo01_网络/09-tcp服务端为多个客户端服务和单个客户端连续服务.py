import socket


def main():
    # 1. 创建监听套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定本地信息
    tcp_server_socket.bind(("", 8080))

    # 3. 让默认的套接字有主动变为被动listen, 默认堵塞
    tcp_server_socket.listen(128)

    while True:
        print("等待新的客户端到来...")

        # 4. 等待客户端链接
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("已连接的客户端:", client_addr)
        while True:
            # 5. 接收消息,
            recv_data = new_client_socket.recv(1024)
            print("客户端发送的消息: %s" % recv_data.decode("utf-8"))

            if recv_data:
                # 发送消息
                new_client_socket.send("hello".encode("utf-8"))
            else:
                break

        # 6. 关闭套接字
        new_client_socket.close()
        print("客户已经服务完毕")
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
