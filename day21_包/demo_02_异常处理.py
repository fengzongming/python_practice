"""
    异常简单学习:
        finally必定会执行, 在return之前执行

"""

def func():
    try:
        # f = open('file', 'w')
        num = 1 / 0
        return True
    except:
        return False
    finally:
        print('执行finally了')
        # f.close()


print(func())
