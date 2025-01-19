def repeat_me(count):
    def decorator_wrapper(func):
        def wrapper(*args):
            counter = count
            while counter >= 1:
                func(*args)
                counter -= 1

        return wrapper

    return decorator_wrapper


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')
