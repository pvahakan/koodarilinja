import random
import os

sanat = ['kello', 'polkupyörä', 'auto', 'mopo', 'lusikka']
kirjoitetut_sanat = []

sanojen_maara = 5

while True:
    os.system('clear')
    print(sanat[random.randint(0, len(sanat)-1)])
    kirjoitetut_sanat.append(input('>> '))
    if len(kirjoitetut_sanat) >= sanojen_maara:
        break

print(kirjoitetut_sanat)