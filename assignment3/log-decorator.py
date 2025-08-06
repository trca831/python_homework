#Task1
import logging
from functools import wraps

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        pos_args = list(args) if args else "none"
        kw_args = kwargs if kwargs else "none"
        result = func(*args, **kwargs)
        logger.log(logging.INFO, f"function: {func_name}")
        logger.log(logging.INFO, f"positional parameters: {pos_args}")
        logger.log(logging.INFO, f"keyword parameters: {kw_args}")
        logger.log(logging.INFO, f"return: {result}\n")
        return result
    return wrapper

@logger_decorator
def say_hello():
    print("Hello, World!")

@logger_decorator
def accepts_positional_args(*args):
    return True

@logger_decorator
def accepts_keyword_args(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    say_hello()
    accepts_positional_args(10, 20, 30)
    accepts_keyword_args(name="Tracy", project="Decorator", status="Running")
