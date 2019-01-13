import socket


def main():
    # 1. 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定自己的信息(ip和端口)
    local_addr = ("", 8081)
    udp_socket.bind(local_addr)

    # 3. 接收数据
    receive_data = udp_socket.recvfrom(1024)

    # 4. 打印数据
    print(receive_data[0].decode("utf-8"))

    # 5. 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
