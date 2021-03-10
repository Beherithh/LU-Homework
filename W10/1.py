h = int(input("height: "))


def print_pyramid(height: int) -> int:
    for i in range(height + 1):
        string = i * "* "
        new_string = string.center(height*2)
        print(new_string)


print_pyramid(h)
