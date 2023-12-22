def decorator_function(function):
    def wrapper():
        function()
        print("I'm decorating your function")
    return wrapper


@decorator_function
def hello_world():
    print("Hello, world!")


hello_world()

# Practical example logging


def logging_module(function):
    def wrapper(*args, **kwargs):
        with open('loggig.txt', 'a+') as f:
            function_name = function.__name__
            returned_value = function(*args, **kwargs)
            print(f"function name is {function_name} and returned value is {returned_value}")
            f.write(f"function name is {function_name} and returned value is {returned_value}\n")
            return returned_value
    return wrapper


@logging_module
def add_function(x, y):
    return x+y


add_function(40,30)


def func1(f):
    f()


def func2():
    print(f"Hello World!")


func1(func2)





