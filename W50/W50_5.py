legs_katalog = {'pigs': 4, 'cows': 4, 'chickens': 2}

pigs = int(input('Amount of pigs: '))
cows = int(input('Amount of cows: '))
chickens = int(input('Amount of chickens: '))

total = pigs * legs_katalog['pigs'] + cows * legs_katalog['cows'] \
        + chickens * legs_katalog['chickens']
print("Total amount of legs:", total)
