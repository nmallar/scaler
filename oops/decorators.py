import functools
import time

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # do something before function call
        value=func()
        # do something after function call
        return value
    return wrapper_decorator


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        # do something before function call
        start_time=time.perf_counter()
        value=func(*args, **kwargs)
        end_time=time.perf_counter()
        # do something after function call
        run_time=end_time-start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args,**kwargs):
        # do something before call
        args_repr=[repr(a) for a in args]
        kwargs_repr=[f"{k}={v!r}" for k,v in kwargs.items()]
        signature=",".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value=func(*args,**kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        #do something after call
        return value
    return wrapper_debug

def slowdown(func):
    """Sleep for 1 second before calling function"""
    @functools.wraps(func)
    def wrapper_slowdown(*args,**kwargs):
        time.sleep(1)
        return func(*args,**kwargs)
        
        
    return wrapper_slowdown