# print_caps.py
def allcaps(func):
    def wrapper():
        result = func()           
        if type(result) != str:   
            raise TypeError("Function must return a string")
        return result.upper()    
    return wrapper
