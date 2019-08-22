# Decorator

"""
Decorator is a function that:
    - takes another function as an arg
    - adds some fucntionality
    - return another function

All of these without altering the source code of the orginal function that being passed in

Used For:
- Logging
- Timing
- Working with 3rd party
- Web routing

Prerequisite:
1. First Class Functions: https://www.youtube.com/watch?v=kr0mpwqttM0
2. Closures: https://www.youtube.com/watch?v=swU3c34d2NQ
"""

# ----
# Function Decorator
# ----


def decorator_function(message):
    def wrapper_function():
        print(message)
    return wrapper_function


hi_func = decorator_function("hi")
bye_func = decorator_function("bye")

hi_func()
bye_func()


# Now lets pass in a function
def decorator_function(orginal_func):
    def wrapper_function():
        print("wrapper executes this before running {} function".format(orginal_func.__name__))
        return orginal_func()
    return wrapper_function


def display():
    print("display function run")


decorated_display = decorator_function(display)
decorated_display()


### 2 Equivalent ways to use decorator ###

"""
def decorator_function(orginal_func):
    def wrapper_function():
        print("execute ")
        return orginal_func()
    return wrapper_function


def display():
    print("display function run")


decorated_display = decorator_function(display)
decorated_display()

OR ----
"""


def decorator_function(orginal_func):
    def wrapper_function(*args, **kwargs):
        # *args, **kwargs: this allows functions to take arbitrage number of inputs
        # it also allows the wrapper decorator to be used with differnet functions
        print("wrapper executes this before running {} function".format(orginal_func.__name__))
        return orginal_func(*args, **kwargs)
    return wrapper_function


@decorator_function
def display():
    print("display function run")


display()


@decorator_function
def display_info(name, age):
    print("display_info run with arguments ({},{})".format(name, age))


display_info("Hugh", 25)
"""wrapper executes this before running display_info function
display_info run with arguments (Hugh,25)"""

# -----
# ALSO, we use Class Decorator instead of Function Decorator:
# But Function Decorator is used more often
# -----


class decorator_class:

    def __init__(self, orginal_func):
        self.orginal_func = orginal_func

    # Call <=> wrapper
    def __call__(self, *args, **kwargs):
        # Note: we using an instance of orginal_func so we NEED to use self.orginal_func
        print("Call Method executes this before running {} function".format(self.orginal_func.__name__))
        return self.orginal_func(*args, **kwargs)


@decorator_class
def display():
    print("display function run")


display()


@decorator_class
def display_info(name, age):
    print("display_info run with arguments ({},{})".format(name, age))


display_info("Hugh", 25)

# -------
# Practical Example:


def my_logger(orginal_func):
    # keep track of how many times a specific function is run
    # and what are the args being passed in
    import logging
    logging.basicConfig(filename="{}.log".format(orginal_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args {0}, and kwargs {1}'.format(args, kwargs))
        return orginal_func(*args, **kwargs)

    return wrapper


def my_timer(orginal_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orginal_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orginal_func.__name__, t2))
        return result

    return wrapper


@my_logger
def display_info(name, age):
    print("display_info run with arguments ({},{})".format(name, age))


display_info("Hugh", 25)


@my_timer
def display_info(name, age):
    print("display_info run with arguments ({},{})".format(name, age))


display_info("Hugh", 25)

# STACKING DECORATOR -------
from functools import wraps
# this would allow us to wrap a decorator with another decorator


def my_logger(orginal_func):
    # keep track of how many times a specific function is run
    # and what are the args being passed in
    import logging
    logging.basicConfig(filename="{}.log".format(orginal_func.__name__), level=logging.INFO)

    # ADD HERE:
    @wraps(orginal_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args {0}, and kwargs {1}'.format(args, kwargs))
        return orginal_func(*args, **kwargs)

    return wrapper


def my_timer(orginal_func):
    import time

    @wraps(orginal_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orginal_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orginal_func.__name__, t2))
        return result

    return wrapper

# Stack:


@my_logger
@my_timer
def display_info(name, age):
    print("display_info run with arguments ({},{})".format(name, age))


display_info("Hugh", 25)
