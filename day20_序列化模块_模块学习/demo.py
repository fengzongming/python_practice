__all__ = ["money", "read"]

money = 100


def read():
    print('in read1', money)


def read2():
    print('in read2')

if __name__ == '__main__':
    read()