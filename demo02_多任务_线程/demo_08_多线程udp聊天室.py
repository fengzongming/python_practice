import time
import socket
import threading


def send_msg(udp_socket, dest_ip, dest_port):
    """发送数据"""
    while True:
        send_data = input("请输入要发送的数据: ")
        udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


def main():
    # 1. 创建socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定本地信息
    udp_socket.bind(("", 8080))

    # 3. 获取接收方的ip和port
    dest_ip = input("请输入接收方ip: ")
    dest_port = int(input("请输入接收方port:"))

    # 发送数据
    t1 = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port))

    # 接收数据
    t2 = threading.Thread(target=recv_msg, args=(udp_socket,))

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
