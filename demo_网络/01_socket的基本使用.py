"""
    socket的使用流程:
        1. 创建一个udp的套接字
        2. 使用套接字收发数据
        3. 关闭套接字

"""
import socket


def main():
    # 创建udp的套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 使用套接字发送数据
    udp_socket.sendto(b"hello world", ("127.0.0.1", 8080))
    print(udp_socket)

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
