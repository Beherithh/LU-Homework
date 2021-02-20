def generator(multiplier):
    for i in range(0, 11):
        yield i * multiplier


x = list(generator(int(input('Enter number: '))))
print(*x, sep='\n')

