import random
import os
import time

sanojen_maara = 8

sanat = ['sedatiivi', 'kesakkoinen', 'selviytyjä', 'hutera', 'siemaista', 
        'korjuun', 'haihatella', 'kuvautua', 'alempi', 'nettotulo', 
        'velvoitetyöllistettävä', 'karambola', 'liftari', 'kuukunanmuna', 
        'ujostelu', 'messinkipuhallin', 'teollisuusmies', 'kielentarkistus', 
        'niemi', 'määräily', 'seinäkirjoitus', 'hopeavalmiste', 'ylivirtaus', 
        'tatti', 'matka', 'euroaika', 'rakennustyömaa', 'pelti', 
        'klamydiatulehdus', 'pahoinvointi', 'esilämmittää', 'hourekuva', 
        'lerpattaa', 'avorauhanen', 'kiinnityskirja', 'puheensorina', 
        'kapealanteinen', 'aikamatkustus', 'peräpuoli', 'kivuta', 
        'totuudellisesti', 'älymystö', 'maakulkuneuvo', 'urheilutoimitus', 
        'jälkiäänitys', 'koskemattomuus', 'sementtitehdas', 'veritulppa', 
        'sienikeitto', 'tasakylkinen', 'limanuljaska', 'senaikainen', 
        'lumppupaperi', 'karkeasanainen', 'hätäännys', 'tuohi', 
        'kirjeenvaihtajajäsen', 'purjosipuli', 'silmityksin', 'nostokurki', 
        'standartti', 'kung-fu', 'ruokalaji', 'pilsneripullo', 'korpiniitty', 
        'kaupita', 'pilotti', 'lankous', 'asetussanat', 'pitkäaikaispotilas', 
        'sotasilla', 'vaihetyö', 'soolohyökkäys', 'karvalakki', 'uurnalehto', 
        'lemmenkohtaus', 'kateellinen', 'lainsäännös', 'joutessa', 
        'lämpöistuin', 'suurikaliiperinen', 'juutalaislähetys', 
        'normaalipaino', 'karvata', 'rullalautailu', 'pro', 'yrityspankki', 
        'varmenne', 'saasteongelma', 'karttaprojektio', 'immenkalvo', 'vieri', 
        'yksisäikeinen', 'luovutus', 'postinjakaja', 'vältellä', 'maalaustekniikka', 
        'riuskuus', 'kanootti', 'heraldiikka']

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

def tulosta_raportti(sanalista, kirjoitetut_sanat, kesto):
    oikein = tarkista_oikeat_sanat(sanalista, kirjoitetut_sanat)
    vaarin = tarkista_vaarat_sanat(sanalista, kirjoitetut_sanat)
    os.system('clear')
    # os.system('cls')
    print(f'Kirjoittamiseen kului aikaa {round(kesto, 2)} sekuntia\n')
    print(f'Kirjoitit oikein {oikein}/{len(kirjoitetut_sanat)} sanaa')
    print(f'Kirjoitit väärin {vaarin}/{len(kirjoitetut_sanat)} sanaa\n')
    input('Paina Enter jatkaaksesi')
    os.system('clear')
    # os.system('cls')

alku = time.time()
while True:
    os.system('clear')
    # os.system('cls')
    print(sanat[random.randint(0, len(sanat)-1)])
    kirjoitetut_sanat.append(input('>> '))
    if len(kirjoitetut_sanat) >= sanojen_maara:
        break
    loppu = time.time()

kesto = loppu - alku
tulosta_raportti(sanat, kirjoitetut_sanat, kesto)
