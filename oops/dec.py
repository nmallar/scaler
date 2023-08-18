import functools
import time

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args,**kwargs):
        # do something before function call
        func(*args,**kwargs)
        value=func(*args,**kwargs)
        # do something after function call
        return value
    return wrapper_do_twice


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args,**kwargs):
        start_time=time.perf_counter()
        val=func(*args,*kwargs)
        end_time=time.perf_counter()
        print(f"Function {func.__name__!r} executed in {end_time:.4f} seconds")
        return val
    return wrapper_timer

def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args,**kwargs):
        
        arg_repr=[repr(arg) for arg in args]
        kwargs_repr=[f"{k!r}={v!r}" for k,v in kwargs.items()]
        signature=",".join(arg_repr+kwargs_repr)
        print(f"Calling {func.__name__!r}({signature})")
        value=func(*args,**kwargs)
        print(f"Function {func.__name__!r} returned {value!r}")
        
    return wrapper_debug
        

