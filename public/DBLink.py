#coding=utf-8
import threading

class Singleton(object):
    _instance_lock=threading.Lock()
    def __init__(self):
        import time
        time.sleep(1)

    @classmethod
    def instance(cls,*args,**kwargs):
        if not hasattr(Singleton,"_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton,"_instance"):
                    Singleton._instance=Singleton(*args,**kwargs)
        return Singleton._instance