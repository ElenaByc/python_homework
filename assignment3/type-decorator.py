def type_converter(type_of_output):
    """Decorator factory that converts function return value to specified type."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator


@type_converter(str)
def return_int():
    """Function that returns integer 5, but decorator converts it to string."""
    return 5


@type_converter(int)
def return_string():
    """Function that returns string 'not a number', decorator tries to convert to int."""
    return "not a number"


# Mainline code
if __name__ == "__main__":
    y = return_int()
    print(type(y).__name__)
    
    try:
        y = return_string()
        print("shouldn't get here!")
    except ValueError:
        print("can't convert that string to an integer!")
