height = int(input('Enter the height: '))
rad = int(input('Enter the radius: '))

vol = 3.14 * rad ** 2 * height
area = 2 * (3.14 * rad ** 2) + height * (2 * 3.14 * rad)

print('Volume:', vol)
print('Area:', area)
