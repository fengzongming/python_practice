import socket


def main():
    # 1. 创建socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定个人信息
    local_addr = ("", 8081)
    udp_socket.bind(local_addr)
    while True:
        print("----欢迎来到udp聊天室----")
        print("1. 发送消息")
        print("2. 接收消息")
        print("0. 退出系统")
        option = input("请选择你要进行的操作:")

        if option == "1":
            # 3. 发送数据
            dest_ip = input("请输入接收信息的ip:")
            dest_port = int(input("请输入接收信息的port:"))
            send_data = input("请输入你要发送的信息: ")
            udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))
        elif option == "2":
            # 4. 接收数据
            recv_data = udp_socket.recvfrom(1024)
            print("%s : %s" % (recv_data[1], recv_data[0].decode("utf-8")))
        elif option == "0":
            break
        else:
            print("你的输入有误, 请重新输入")
    udp_socket.close()


if __name__ == '__main__':
    main()
