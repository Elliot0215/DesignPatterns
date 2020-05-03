import threading
import time

class SingletonPatterns(object):
    lock = threading.Lock()
    def __init__(self,*args, **kwargs):
        time.sleep(2)

    '''
    @classmethod
    def getInstance(cls,*args, **kwargs):
        with SingletonPatterns.lock:
            if not hasattr(SingletonPatterns,"_instance"):
                SingletonPatterns._instance = SingletonPatterns(*args, **kwargs)
        return SingletonPatterns._instance
    '''

    def __new__(cls, *args, **kwargs):
        with SingletonPatterns.lock:
            if not hasattr(SingletonPatterns,"_instance"):
                SingletonPatterns._instance = super(SingletonPatterns,cls).__new__(cls)
        return SingletonPatterns._instance


def task(arg):
    p1 = SingletonPatterns()
    print(p1)

for i in range(10):
    t = threading.Thread(target=task, args=[i, ])
    t.start()
