sec = int(input('Seconds: '))

hh = sec // 3600
mm = sec % 3600 // 60
ss = sec % 60

print(hh, 'hours', mm, 'minutes', ss, 'seconds')
