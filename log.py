# log.py
import time  

def timestamp(func):
    def wrapper():
        print(time.ctime())  
        func()                
    return wrapper

