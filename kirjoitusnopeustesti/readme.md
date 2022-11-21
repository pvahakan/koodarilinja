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