def print_function_name(func):
    def the_wrapper():
        print('Executing print_ok: ')
        func()
    return the_wrapper


@print_function_name
def print_ok():
    print('Ok')


print(help(print_ok))
