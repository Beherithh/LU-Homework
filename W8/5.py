def generator(start, end):
    for i in range(start, end + 1):
        if i < 2:
            continue
        elif i == 2:
            yield 2
        else:
            for z in range(2, int(i ** 0.5)+1):
                if i % z == 0:
                    break
            else:
                yield i


x = list(generator(int(input('Start: ')), int(input('End: '))))
print(*x, sep='\n')

