import logging

# One time setup
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    """Decorator that logs function name, parameters, and return value."""
    def wrapper(*args, **kwargs):
        # Log function name
        logger.log(logging.INFO, f"function: {func.__name__}")
        
        # Log positional parameters
        if args:
            logger.log(logging.INFO, f"positional parameters: {list(args)}")
        else:
            logger.log(logging.INFO, "positional parameters: none")
        
        # Log keyword parameters
        if kwargs:
            logger.log(logging.INFO, f"keyword parameters: {kwargs}")
        else:
            logger.log(logging.INFO, "keyword parameters: none")
        
        # Call the function and get return value
        result = func(*args, **kwargs)
        
        # Log return value
        logger.log(logging.INFO, f"return: {result}")
        
        return result
    
    return wrapper


@logger_decorator
def function_no_params():
    """Function that takes no parameters and returns nothing."""
    print("Hello, World!")


@logger_decorator
def function_positional_args(*args):
    """Function that takes variable positional arguments and returns True."""
    return True


@logger_decorator
def function_keyword_args(**kwargs):
    """Function that takes no positional args and variable keyword args, returns logger_decorator."""
    return logger_decorator


# Mainline code
if __name__ == "__main__":
    # Call function with no parameters
    function_no_params()
    
    # Call function with positional arguments
    function_positional_args(1, 2, 3, "test")
    
    # Call function with keyword arguments
    function_keyword_args(name="Alice", age=30, city="New York")
