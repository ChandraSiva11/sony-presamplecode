"""Multi processing string"""
import time
import multiprocessing


def function1():
    """Function1 Doc string"""
    while True:
        print('Function1 called')
        time.sleep(1)


def function2():
    """Function1 Doc string"""
    while True:
        print('Function2 called')
        time.sleep(1)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=function1)
    p2 = multiprocessing.Process(target=function2)
    p1.start()
    p2.start()
    # p1.join()
    # p2.join()
