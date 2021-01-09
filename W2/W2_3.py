first = int(input("Start: "))
second = int(input("End: "))
total = 0

for i in range(first, second + 1):
    if i % 13 == 0 or i % 4 > 0 and 99 < i < 1000:
        continue
    elif 999 < i < 10000 and i % 7000 == 0:
        break
    else:
        total += i
print(f"Sum: {total}")
