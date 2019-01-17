import os
import time
import multiprocessing


def test1():
    while True:
        print("--- in 子进程 pid = %d, 父进程 pid = %d" % (os.getpid(), os.getppid()))
        time.sleep(1)


def main():
    print("--- in 子进程 pid = %d, 父进程 pid = %d" % (os.getpid(), os.getppid()))
    p1 = multiprocessing.Process(target=test1)
    p1.start()


if __name__ == '__main__':
    main()
