# Tehtävä 0 - Testataan, että kaikki toimii

Aloitetaan ohjelmoinnin opiskelu Python-ohjelmointikielellä. Ohjelmointia voidaan harjoitella opiskelija-kannettavista löytyvän Idle-ohjelman avulla.

Tee ensin kannettavan hakemistoon kansio "Ohjelmointi". Luo "Ohjelmointi"-kansion sisään toinen kansio "Aloitus".

Avaa Idle, varmista että avaat Python3-version. Avaa Idlestä editori (jos se ei auennut valmiiksi) kohdasta "File" --> "New file". Nyt sinulla pitäisi olla auki kaksi ikkunaa. Tyhjä ikkuna on editori. Siihen kirjoitetaan koodi. Toinen ikkuna on Python-tulkki, joka kääntää ja suorittaa kirjoittamasi koodin.

Kirjoita editoriin seuraava rivi. Ole tarkkana, että kaikki merkit ovat juuri niin kuin alla.

```python
print('Hello world!')
```

Tallenna kooditiedosto (File --> Save as) kansioon "Aloitus", jonka loit hetki sitten. Anna tiedostolle nimeksi tehtava_0.py

Huomaa, että ohjelmoinnissa ei kannata käyttää ääkkösiä. Joskus ohjelmat menevät sekaisin ääkkösistä, joten on turvallisempaa olla käyttämättä niitä kooditiedoston sisällä (pois lukien kommentit) ja tiedostonimissä.

Seuraavaksi koodi pitää suorittaa. Kun olet tallentanut tiedoston, valitse "Run" --> "Run module" (tai paina F5). Nyt toisessa Idlen ikkunassa, tulkissa, pitäisi näkyä tulostettuna teksti "Hello world!".

Jos tulostus näkyi, kaikki toimii kuten pitää ja voidaan jatkaa eteenpäin!

# Tehtävä 1 - Neliön piirtäminen

Ohjelmointi on käytännössä yksiselitteisten ohjeiden antamista tietokoneelle. Ohjeet annetaan jollakin ohjelmointikielellä.

Tässä tehtävässä sinun tulee piirtää neliö. Neliön sivun pituus on 50. Käytä piirtämiseen Pythonin Turtle-kirjastoa.

# Tehtävä 2 - Kaksi neliötä

Tehtävänäsi on piirtää kaksi neliötä eri puolille piirtoikkunaa. 

- Ensimmäinen neliö piirretään vasempaan yläreunaan ja sen sivun pituus on 60. 
- Toinen neliö piirretään oikeaan alareunaaan ja sen sivun pituus on 20. 

*Huom! Neliöiden ei tarvitse olla tarkalleen reunassa, riittää, että ne ovat oikealla suunnalla.*

# Tehtävä 3 - Kuusikulmio

a) Piirrä kuusikulmio.

b) Väritä kuusikulmio punaiseksi.

Monikulmion yhden sisäkulman suuruus voidaan laskea seuraavasti: $$kulma = \frac{180 \cdot (n - 2)}{n}$$, missä $n$ on kulmien lukumäärä.

Huom! Turtlessa käännöksessä käytettävä kulma on ulkokulma. Se saadaan laskettua $$180 - kulma$$.

# Tehtävä 4 - Ruotsin lippu

Piirrä ja väritä ruotsin lippu.

# Tehtävä 5 - Muutettava neliö

Muokkaa neliön piirtävää koodia siten, että neliön kokoa voi muuttaa tekemällä muutoksia ainoastaan yhdelle koodiriville.

# Tehtävä 6 - Tietoa käyttäjältä

Piirrä ympyrä ja väritä se. Väri pitää kysyä käyttäjältä ohjelman suorituksen aluksi. Riittää, että ohjelma toimii käyttäjän syöttäessä Turtlen tunnistaman englanninkielisen värin, esim. "red".

# Tehtävä 7 - Suorakulmainen kolmio

a) Tee ohjelma, joka piirtää suorakulmaisen kolmion. Ohjelman tulee kysyä käyttäjältä kateettien pituudet, jonka jälkeen ohjelma laskee hypotenuusan pituuden. Hypotenuusan pituuden saat Pythagoraan lauseen avulla seuraavasti:

$$c = \sqrt(a^2 + b^2)$$

missä $a$ ja $b$ ovat kateettien pituudet. Pythonissa neliöjuuren voi laskea math-kirjaston funktiolla sqrt() ja potenssiinkorotus tehdään kahdella kertomerkillä **.

Piirrä tehtävässä ensin kaksi kateettia. Terävään kulmaan tarvittavan käännöksen voit laskea seuraavasti:

```python
kulma = 180 - math.atan2(a, b) * 180 / math.pi
```

b) Muokkaa ohjelmaa siten, että se kysyy käyttäjältä millä värillä kolmio väritetään. Tulosta yhteenveto kuviosta (eli kateettien ja hypotenuusan pituudet sekä täyttöväri) ennen piirtämistä.


# Tehtävä 8

Piirrä jokin haluamasi kuvio. Ohjelman tulee kysyä käyttäjältä kynän piirtonopeus (kokonaisluku 0-9) ja piirrosnopeuden tulee muuttua käyttäjän syötteen mukaisesti.

# Tehtävä 9

a) Piirrä neliö. Neliön sivun pituus tulee olla muuttujassa.

b) Laske neliön pinta-ala ja tulosta se näytölle.

c) Laske sellaisen ympyrän säde, jonka pinta-ala on sama kuin neliön pinta-ala. Tulosta näytölle laskemasi ympyrän säde. Säde lasketaan pinta-alasta (A) seuraavasti:

$$r = \sqrt(\frac{A}{\pi})$$

Koodiin voit kirjoittaa sen tällä tavalla

```python
sade = math.sqrt(pinta-ala / math.pi)
```

d) Piirrä c-kohdassa saamasi ympyrä neliön kanssa samaan kuvaan. Varmista, että piirtäminen toimii, kun vaihdat neliön sivun pituutta muuttujassa.

e) Muokkaa ohjelma siten, että neliön sivun pituus kysytään käyttäjältä ohjelman aluksi.