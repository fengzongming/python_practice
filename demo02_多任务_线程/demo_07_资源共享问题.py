import time
import threading

g_num = 0
mutex = threading.Lock()


def test1(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("in test1 g_num = %d" % g_num)


def test2(num):
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("in test1 g_num = %d" % g_num)


def main():
    t1 = threading.Thread(target=test1, args=(1000000, ))
    t2 = threading.Thread(target=test2, args=(1000000, ))

    t1.start()
    t2.start()

    # 等待上面2个线程执行完毕
    time.sleep(2)

    print("in main g_num = %d" % g_num)


if __name__ == '__main__':
    main()
