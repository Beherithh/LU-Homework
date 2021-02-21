def generator(start, end):
    for i in range(start, end + 1):
        marker = 0
        if i < 2:
            pass
        elif i == 2:
            yield 2
        else:
            for z in range(2, int(i ** 0.5)+1):
                if i % z == 0:
                    marker = 1
                    break
            if marker == 0:
                yield i


x = list(generator(int(input('Start: ')), int(input('End: '))))
print(*x, sep='\n')

