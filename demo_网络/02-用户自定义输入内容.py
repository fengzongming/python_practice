import socket


def main():
    # 创建一个udp的套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    local_addr = ("", 8080)
    udp_socket.bind(local_addr)

    # 使用套接字发送数据
    while True:
        content = input("请输入你要发送的内容: ")

        if content == "quit" or content == "exit":
            break

        udp_socket.sendto(content.encode("utf-8"), ("127.0.0.1", 8081))

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
