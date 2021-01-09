first = int(input("Start: "))
second = int(input("End: "))
divider = int(input("Divider: "))
counter = 0
for i in range(first, second + 1):
    if i % divider == 0:
        counter += 1

print(f'{counter} numbers between {first} and {second}'
      f' can be devided by {divider}')
