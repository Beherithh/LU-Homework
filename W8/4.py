def print_function_name(func):
    def the_wrapper():
        print(f'Executing {func.__name__}')
        func()
    return the_wrapper


@print_function_name
def print_ok():
    print('Ok')


print_ok()
