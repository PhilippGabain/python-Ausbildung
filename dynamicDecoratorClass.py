"""
Decorators can be used to extend functions from external libraries or for debugging
"""
import functools
import time


class dynamic_decorator:
    def __init__(self, wrappername, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.wrapperFunction = None
        if self.wrapperexists(wrappername):
            self.wrapperFunction = getattr(self, wrappername)

    def wrapperexists(self, wrappername):
        return hasattr(self, wrappername)

    def __call__(self, func):
        @functools.wraps(func)  # Copies metadata from func to wrapper
        def wrapper(*args, **kwargs):
            if self.wrapperFunction:
                return self.wrapperFunction(func, *args, **kwargs)
            return func(*args, **kwargs)  # Default case (no wrapper)
        return wrapper

    def set_arguments(self, wrappername, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        if self.wrapperexists(wrappername):
            self.wrapperFunction = getattr(self, wrappername)

    def benchmark(self, func, *args, **kwargs):
        t = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed_time = time.perf_counter() - t
        print(f"{func.__name__} took {elapsed_time:.6f} seconds")
        return result

    def logging(self, func, *args, **kwargs):
        print(f"I can still access the argument given in the decorator args: {self.args}, kwargs: {kwargs}")
        print(f"the function {func.__name__} has the arguments args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result


decorator = dynamic_decorator("benchmark", 1, 1, "Hi")

@decorator
def function(*args, **kwargs):
    print(f"I am a function with args: {args} and kwargs: {kwargs}")

function("These are pretty cool function arguments", {2, 4, 5})
decorator.set_arguments("logging", 3, 6, "bye")
function("I changed these function arguments")
