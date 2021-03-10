counter = []


def call_counter(func):
    def decor():
        global counter
        counter.append(func.__name__)
        count = counter.count(func.__name__)
        print(f"Function {func.__name__} has been called {count} times")
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
