counter = []


def call_counter(func):
    counter = 0
    def decor():
        nonlocal counter
        counter += 1
        print(f"Function {func.__name__} has been called {counter} times")
        func()
    return decor


@call_counter
def print_ok():
    print('OK')


@call_counter
def print_hi():
    print('Hi')


print_ok()
print_ok()
print_hi()
print_ok()
