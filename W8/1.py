list_3 = [x for x in range(1, 101) if x % 3 != 0]
list_3map = list(filter(lambda x: x % 3 != 0, range(1, 101))) # 2nd option
print(list_3)
print(list_3map)
