import random
import time
import os

# sanat = ['hei', 'moi', 'kyllä', 'ei', 'tervetuloa']
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
    cpm = laske_merkit_minuutissa(kirjoitetut_sanat, kesto)
    wpm = laske_sanat_minuutissa(kirjoitetut_sanat, kesto)
    os.system('clear')
    print(f'Kirjoittamiseen kului aikaa {round(kesto, 2)} sekuntia\n')
    print(f'Kirjoitit oikein {oikein}/{len(kirjoitetut_sanat)} sanaa')
    print(f'Kirjoitit väärin {vaarin}/{len(kirjoitetut_sanat)} sanaa\n')
    print(f'Kirjoitusnopeutesi on {round(cpm)} merkkiä/min eli {round(wpm)} sanaa/min\n')
    input('Paina Enter lopettaaksesi')
    os.system('clear')

def laske_merkit_minuutissa(kirjoitetut_sanat, kesto):
    kesto = kesto / 60 # Muutetaan minuuteiksi
    merkkien_maara = 0
    for sana in kirjoitetut_sanat:
        merkkien_maara += len(sana)

    return merkkien_maara / kesto

def laske_sanat_minuutissa(kirjoitetut_sanat, kesto):
    kesto = kesto / 60 # Muutetaan minuuteiksi
    merkkien_maara = 0
    for sana in kirjoitetut_sanat:
        merkkien_maara += len(sana)
    
    sanoja = round(merkkien_maara / 5)
    return sanoja / kesto

## PÄÄOHJELMA

os.system('clear')
print('Tällä ohjelmalla voit testata kirjoitusnopeutesi.')
print()
print('Ohjelma arpoo sinulle satunnaisesti haluamasi määrän sanoja')
print('jotka sinun tulee kirjoittaa ja hyväksyä Enterillä.')
print()
print('Testin jälkeen ohjelma tulostaa kirjoitusnopeutesi yksiköissä')
print('merkkiä / min sekä sanaa / min. Yksi sana vastaa viittä (5) merkkiä.')
print()

sanojen_maara = int(input('Anna kirjoitettavien sanojen määrä: '))
aloitusaika = time.time()

while True:
    # os.system('cls') # Windows
    os.system('clear') # Linux
    print(sanat[random.randint(0, len(sanat)-1)])
    sana = input('>> ')
    kirjoitetut_sanat.append(sana)

    if len(kirjoitetut_sanat) >= sanojen_maara:
        lopetusaika = time.time()
        break


kesto = lopetusaika - aloitusaika
tulosta_raportti(sanat, kirjoitetut_sanat, kesto)