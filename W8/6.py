def my_range(start, end, step=1):
    if step > 0:
        while start < end:
            yield start
            start += step
    elif step < 0:
        while start > end:
            yield start
            start += step


x = list(my_range(int(input('Start: ')), int(input('End: ')), int(input('Step: '))))
print(x)
