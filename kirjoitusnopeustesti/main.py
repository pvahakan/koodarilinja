import random
import os

sanat = ['hei', 'moi', 'kyllä', 'ei', 'tervetuloa']
kirjoitetut_sanat = []

def tarkista_oikeat_sanat(kirjoitetut_sanat):
    oikein = 0
    for sana in kirjoitetut_sanat:
        if sana in sanat:
            oikein += 1
    return oikein

def tarkista_vaarat_sanat(kirjoitetut_sanat):
    oikein = tarkista_oikeat_sanat(kirjoitetut_sanat)
    return len(kirjoitetut_sanat) - oikein

def tulosta_raportti(kirjoitetut_sanat):
    oikein = tarkista_oikeat_sanat(kirjoitetut_sanat)
    vaarin = tarkista_vaarat_sanat(kirjoitetut_sanat)
    print(f'Kirjoitit oikein {oikein}/{len(kirjoitetut_sanat)} sanaa')
    print(f'Kirjoitit väärin {vaarin}/{len(kirjoitetut_sanat)} sanaa')

i = 0
while i < 5:
    os.system('cls') # Windows
    # os.system('clear') # Linux
    print(sanat[random.randint(0, len(sanat)-1)])
    sana = input('>> ')
    kirjoitetut_sanat.append(sana)

    if sana == 'q':
        break

    i += 1

tulosta_raportti(kirjoitetut_sanat)