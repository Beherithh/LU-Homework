d = int(input('Dālderi: '))
g = int(input('Graši: '))
s = int(input('Santīmi: '))

s = (d * 37 + g) * 162 + s
nd = s // 100
ns = s % 100

print('Jaunie Dālderi:', nd)
print('Jaunie Santīmi:', ns)
