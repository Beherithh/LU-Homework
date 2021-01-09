first = int(input("Start: "))
second = int(input("End: "))
sum = 0
if first % 2 != 0:
    first += 1
for i in range(first, second + 1, 2):
    sum += i
print(sum)
