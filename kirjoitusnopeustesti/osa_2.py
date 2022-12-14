import random
import os

sanojen_maara = 5

sanat = ['kello', 'polkupyörä', 'auto', 'mopo', 'lusikka']
kirjoitetut_sanat = []

def tarkista_oikeat_sanat(sanalista, kirjoitetut_sanat):
    oikein = 0
    for sana in kirjoitetut_sanat:
        if sana in sanalista:
            oikein += 1
    return oikein

def tarkista_vaarat_sanat(sanalista, kirjoitetut_sanat):
    oikein = tarkista_oikeat_sanat(sanalista, kirjoitetut_sanat)
    return len(kirjoitetut_sanat) - oikein

def tulosta_raportti(sanalista, kirjoitetut_sanat):
    oikein = tarkista_oikeat_sanat(sanalista, kirjoitetut_sanat)
    vaarin = tarkista_vaarat_sanat(sanalista, kirjoitetut_sanat)
    os.system('clear')
    # os.system('cls')
    print(f'Kirjoitit oikein {oikein}/{len(kirjoitetut_sanat)} sanaa')
    print(f'Kirjoitit väärin {vaarin}/{len(kirjoitetut_sanat)} sanaa\n')
    input('Paina Enter jatkaaksesi')
    os.system('clear')
    # os.system('cls')

while True:
    os.system('clear')
    # os.system('cls')
    print(sanat[random.randint(0, len(sanat)-1)])
    kirjoitetut_sanat.append(input('>> '))
    if len(kirjoitetut_sanat) >= sanojen_maara:
        break

tulosta_raportti(sanat, kirjoitetut_sanat)
