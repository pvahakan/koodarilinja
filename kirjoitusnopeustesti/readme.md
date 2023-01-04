# Kirjoitusnopeuspeli

Seuraavaksi tavoite on tehdä kirjoitustarkkuutta ja nopeutta mittaava peli, jota voidaan pelata komentoriviltä. Pelissä annetaan lista sanoja, joita esitetään käyttäjälle satunnaisessa järjestyksessä. Pelaaja kirjoittaa hänelle esitetyn sanan.

Pelissä voi valita, kuinka monta sanaa pelaaja haluaa kirjoittaa. Kun annettu sanamäärä on täysi, ohjelma tulostaa raportin näytölle. Raportissa näkyy kuinka monta sanoista meni oikein ja kuinka monta väärin. Lisäksi peli laskee kirjoitusnopeuden, eli kuinka monta merkkiä käyttäjä on kirjoittanut minuutissa sekä kuinka monta sanaa käyttäjä kirjoittaa minuutissa (yksi sana on viisi merkkiä).

# Pelin toteuttaminen

Tehtävän suorittamisen helpottamiseksi olen palastellut ongelmaa osiin tehtävien muodossa. Suorittamalla alla olevia tehtäviä järjestyksessä, pääset vaihe vaiheelta lähemmäksi lopullista peliä.

Aluksi luodaan tehtävän ratkaisussa tarvittavia funktioita ja pikku hiljaa niitä kasataan yhteen toimivaksi kokonaisuudeksi. Lue tehtävien ohjeet huolellisesti, jotta tiedät mitä pitää tehdä missäkin vaiheessa.

# Tehtävä 1 - Oikeinkirjoitettujen sanojen määrä

Tehtävänä on luoda funktio, joka laskee ja palauttaa oikein kirjoitettujen sanojen määrän. **HUOM! Vielä ei tarvitse toteuttaa kirjoittamista. Voit kirjoittaa suoraan koodiin käyttäjän kirjoittamat sanat listana. Toteutus, jossa käyttäjä joutuu itse kirjoittamaan sanat lisätään myöhemmin.**

Funktio ottaa argumentikseen kaksi listaa. Toisessa listassa on kirjoitetut sanat ja toisessa listassa kaikki mahdolliset testissä olevat sanat.

Oikeinkirjoitus tutkitaan siten, että käydään käyttäjän kirjoittamat sanat läpi. Mikäli käyttäjän kirjoittama sana löytyy alkuperäisestä sanalistasta, on käyttäjä kirjoittanut sanan oikein. Muussa tapauksessa sana on kirjoitettu väärin.

Funktion tulee palauttaa oikeinkirjoitettujen sanojen määrä. Alla esimerkki testipääohjelmasta, jolla voit testata funktion toimintaa.

```python
kaikki_sanat = ['hei', 'moi', 'terve', 'kiitos']
kirjoitetut_sanat = ['moi', 'tevre', 'kiitos', 'moi', 'hhei']

oikeat_sanat = laske_oikeat_sanat(kaikki_sanat, kirjoitetut_sanat)
print(oikeat_sanat) # Tämä tulostaa 3
```

Tässä täytyy tutkia, onko joku tietty alkio toisessa listassa vai ei. Eräs tapa on käyttää Pythonin ``in``-avainsanaa, joka toimii seuraavasti.

```python
lukulista = [1, 2, 3, 4, 5]
numero = 3
toinen_numero = 8

print(numero in lukulista) # Tulostaa True
print(toinen_numero in lukulista) # Tulostaa False

# In-avainsanaa voidaan käyttää myös ehtolauseessa
if numero in lukulista:
    # Tee jotakin, jos numero löytyy listasta
```

# Tehtävä 2 - Väärin kirjoitettujen sanojen määrä

Luo funktio, joka laskee ja palauttaa väärin kirjoitettujen sanojen määrän. Funktio ottaa kaksi argumenttia, listan käyttäjän kirjoittamia sanoja sekä listan, jossa on kaikki mahdolliset sanat. Voit hyödyntää edellisen tehtävän tietoja tai käyttää hyväksi tietoa, että väärien sanojen määrä saadaan, kun kaikista sanoista vähennetään oikeat sanat.

Alla esimerkki funktion toiminnasta:
```python
kaikki_sanat = ['hei', 'moi', 'terve', 'kiitos']
kirjoitetut_sanat = ['moi', 'tevre', 'kiitos', 'moi', 'hhei']

vaarat_sanat = laske_vaarat_sanat(kaikki_sanat, kirjoitetut_sanat)
print(vaarat_sanat) # Tämä tulostaa 2
```

# Tehtävä 3 - Raportin tulostaminen

Luo funktio, joka tulostaa raportin kirjoitetuista sanoista. Tässä vaiheessa riittää, että raportissa tulostetaan oikeinkirjoitettujen ja väärinkirjoitettujen sanojen määrä.

Funktio ottaa argumentikseen kaksi listaa. Toisessa listassa on käyttäjän kirjoittamat sanat ja toisessa kaikki mahdolliset sanat. Funktiossa lasketaan kuinka monta sanaa on kirjoitettu oikein ja kuinka monta väärin. Lisäksi funktiossa tulostetaan oikein ja väärin kirjoitettujen sanojen määrä kaikista sanoista. **HUOM! Hyödynnä tässä tehtävässä aiemmin tekemiäsi funktioita!**

Alla esimerkki funktion toiminnasta.

Pääohjelma:
```python
kaikki_sanat = ['hei', 'moi', 'terve', 'kiitos']
kirjoitetut_sanat = ['moi', 'tevre', 'kiitos', 'moi', 'hhei']

tulosta_raportti(kaikki_sanat, kirjoitetut_sanat)
```

Tulostus:
```
Kirjoitit oikein 3/5 sanaa
Kirjoitit väärin 2/5 sanaa
```

**Varmista, että ohjelma toimii, jos sanalistoja muutetaan!**

# Tehtävä 4 - Sanojen kysyminen käyttäjältä

Seuraavaksi lähdetään rakentamaan kirjoitustestin runkoa. **Tyhjennä aikaisemmin tekemäsi pääohjelma, mutta jätä funktiot samaan tiedostoon. Tarvitset niitä myöhemmin! Tämä tehtävä kirjoitetaan siis pääohjelmaan.**

a) Luo lista, jossa on vähintään viisi sanaa. Voit keksiä sanat itse. Näitä sanoja käytetään, jotta ohjelman toiminta saadaan halutunlaiseksi. Sanat korvataan myöhemmin kattavammalla listalla.

b) Luo muuttuja, joka sisältää tiedon kuinka monta sanaa käyttäjän pyydetään kirjoittamaan. Aseta aluksi muuttujan arvoksi 5. Tulosta näytölle satunnaisesti joku listan sanoista tässä tapauksessa viisi kertaa peräkkäin. Käytä toistorakenteena while-silmukkaa. **Toteuta tämä sillä tavalla, että sanalistan kokoa voi muuttaa ja silti kaikilla sanoilla on mahdollisuus tulostua näytölle!** Tämän suoritettuasi sinulla pitäisi näkyä näytöllä allekkain viisi sanaa, jotka ovat satunnaisesti valittu a-kohdassa kirjoittamastasi sanalistasta. **Huom! Kyse on satunnaisluvuista, jolloin sama sana voi näkyä useamman kerran, etenkin jos sanalista on pieni.**

Varmista, että ohjelmassa toimii seuraavat asiat:

- Sanalistan kokoa voi muuttaa ja kaikilla sanoilla on mahdollisuus päätyä tulostettavaksi.
- Tulostettavien sanojen määrää voi muuttaa vaihtamalla ainoastaan muuttujan arvoa.

Tarvitset seuraavia asioita tehtävässä:
```python
import random

satunnaisluku = random.randint(0, 5) # Satunnaisluku nollan ja viiden väliltä

lista_sanoja = ['moi', 'hei', 'terve']
listan_pituus = len(lista_sanoja)
print(lista_sanoja[0]) # Tulostaa listan 1. alkion
print(lista_sanoja[listan_pituus - 1]) # Tulostaa listan viimeisen alkion
```

c) Luo tyhjä lista, johon tallennat käyttäjän kirjoittamat sanat. Kysy tulostettu sana käyttäjältä ja tallenna käyttäjän kirjoittama sana listaan. Tulosta ohjelman lopuksi listan sisältö.

d) Muokkaa toteutusta siten, että aina uuden sanan välissä komentorivi tyhjennetään. Näytöllä tulee näkyä siis vain yksi sana ja kohta, johon käyttäjä voi kirjoittaa sanan. Komentorivi voidaan tyhjentää ``clear``-komennolla (Windowsissa ``cls``). Pythonilla voit suorittaa komennon seuraavasti:

```python
import os
os.system('clear') # Linux
os.system('cls') # Windows
```

Lopullinen ohjelman suoritus näyttää tältä (sanalistassa sanat ['kello', 'polkupyörä', 'auto', 'mopo', 'lusikka']):

![kirjoitustesti.gif](./kirjoitusnopeustesti_osa_1.gif)

# Tehtävä 5 - Raportin tulostaminen kirjoitettujen sanojen pohjalta

Lisää edelliseen tehtävään toteutus, jossa tarkistetaan käyttäjän kirjoittamat sanat ja tulostetaan raportti niistä. Eli kun ohjelma suoritetaan, käyttäjälle syötetään haluttu määrä sanoja satunnaisesti ohjelmassa olevasta sanalistasta. Käyttäjä kirjoittaa sanat, jonka jälkeen ohjelma tutkii kuinka moni sana kirjoitettiin oikein ja kuinka moni väärin sekä tulostaa lopuksi raportin. Raportti näytetään niin kauan, kunnes käyttäjä painaa Enter. Tämän jälkeen näyttö tyhjennetään ja ohjelman suoritus päättyy. *Vihje: Odottamisen Enterin painamiseen asti voi toteuttaa helposti ``input``-komennon avulla.*

Tehtävän jälkeen ohjelman tulisi näyttää tältä:

![kirjoitustesti_2.gif](./kirjoitusnopeustesti_osa_2.gif)

# Tehtävä 6 - Laajennettu sanalista

Varmista, että ohjelma toimii riippumatta annettuja sanoja sisältävän listan koosta sekä kirjoitettavien sanojen määrästä. 

1. Vaihda kirjoitettavien sanojen määräksi 8.
2. Vaihda ohjelmaasi alla oleva lista sanoja. Sanat (100 kpl) on generoitu satunnaisesti kotimaisten kielten keskuksen (Kotus) ylläpitämästä suomen kielen sanalistasta, joka sisältää yhteensä yli 90 000 sanaa.

Kun suoritat ohjelman, pitäisi ohjelman esittää sinulle satunnaisesti 8 sanaa alla olevasta listasta. **Tarkista, että sanojen määrä täsmää myös raportissa!**

```python
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
```

# Tehtävä 7 - Kirjoituksen keston mittaaminen

a) Seuraavaksi mitataan, kuinka kauan kirjoittamisessa kestää. Tarvitset keston mittaamiseen pythonin ``time``-kirjastoa, ota se käyttöön komennolla ``import time``.

Tietyn ajanhetken (ikään kuin kellonaika) voit määrittää seuraavasti:

```python
import time

ajanhetki = time.time()
```

Logiikka ajan mittaamisessa menee seuraavasti:

- Määritä kaksi eri ajanhetkeä, milloin kirjoittaminen alkaa ja milloin se päättyy.
- Kirjoittamisen kesto saadaan loppuhetken ja alkuhetken erotuksena. Yllä olevalla tavalla toteutettuna kesto saadaan sekunteina.

b) Lisää kirjoittamisen kesto raportin tulostukseen. Tätä varten sinun tulee muokata raportin tulostusfunktiota siten, että se ottaa kolmanneksi argumentikseen kirjoittamisen keston. Funktion määrittelyn tulisi näyttää tältä:

```python
def tulosta_raportti(sanalista, kirjoitetut_sanat, kesto):
    # Oma toteutuksesi funktiolle tähän
```

**Pyöristä kesto kahden desimaalin tarkkuuteen!** Pyöristäminen voidaan tehdä ``round-komennolla``:

```python
pitka_desimaaliluku = 1.23456789
pyoristetty_luku = round(pitka_desimaaliluku, 3)
print(pyoristetty_luku) # Tulostaa luvun 1.23
```

Muokkaa raportin tulostaminen siten, että raportin aluksi näkyy kirjoittamiseen kulunut aika. Kahdeksan sanan testissä suorituksen pitäisi näyttää tehtävän jälkeen seuraavalta.

![kirjoitustesti_3.gif](./kirjoitusnopeustesti_osa_3.gif)

# Tehtävä 8 - Kirjoitusnopeuden laskeminen osa 1

Luo funktio, joka laskee kuinka monta merkkiä käyttäjä kirjoittaa minuutissa. Funktio ottaa argumentikseen listan käyttäjän kirjoittamia sanoja sekä kirjoitusajan sekunteina ja palauttaa kuinka monta merkkiä käyttäjä kirjoitti minuutissa.

Funktion määrittely näyttää seuraavalta.

```python
def laske_merkit_minuutissa(kirjoitetut_sanat, kesto):
    # Toteuta funktio tähän
```

Funktiossa tulee muuttaa sekunnit minuuteiksi sekä laskea kirjoitettujen sanojen merkit. Yksittäisen sanan merkit saat selville funktion ``len()`` avulla. Esimerkiksi

```python
print(len('unelmaduuni')) # tulostaisi 11
```

Sinun pitää siis käydä kaikki kirjoitetut sanat läpi ja tallentaa sanojen yhteispituus muuttujaan.

Voit testata funktiota kommentoimalla vanhan pääohjelman pois ja lisäämällä pääohjelmaan seuraavan koodinpätkän. Jos tulostus seuraavalla koodilla on 55.0, funktio toimii todennäköisesti oikein.

```python
kirjoitetut_sanat = ['moi', 'hei', 'kyllä']
kesto = 12 # sekunteja

print(laske_merkit_minuutissa(kirjoitetut_sanat, kesto)) # Tulostaa 55.0
```

# Tehtävä 9 - Kirjoitusnopeuden laskeminen osa 2

Luo toinen funktio, joka laskee sanojen määrän minuutissa. **Huom! Tässä sana tarkoittaa viiden merkin joukkoa!** Eli laskennassa jokaisessa sanassa on viisi merkkiä. Esimerkiksi sana "curlingmestaruus" sisältää yli 3 sanaa (16 merkkiä).

Funktio ottaa argumentikseen listan kirjoitettuja sanoja sekä kirjoittamiseen kuluneen ajan sekunteina. Funktio palauttaa kirjoitettujen sanojen määrän minuutissa. Funktion määrittely näyttää seuraavalta:

```python
def laske_sanat_minuutissa(kirjoitetut_sanat, kesto):
    # Toteutus tähän
```

Käytä hyväksesi edellisen tehtävän ratkaisua. Edelliseen tehtävään verrattuna tässä tehtävässä tulee selvittää, kuinka monta viiden merkin "sanaa" kirjoitetut sanat sisältävät. Voit pyöristää sanojen määrän lähimpään kokonaislukuun.

Testaa funktiota seuraavalla ohjelmalla, jonka pitäisi tulostaa 10.0.

```python
kirjoitetut_sanat = ['moi', 'hei', 'kyllä']
kesto = 12 # sekunteja

print(laske_sanat_minuutissa(kirjoitetut_sanat, kesto)) # Tulostaa 10.0
```