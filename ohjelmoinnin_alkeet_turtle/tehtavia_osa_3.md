# Tehtävä 1 - Neliönpiirtofunktio

a) Tee funktio ``piirra_nelio()``, jonka avulla voidaan piirtää neliö.

b) Muokkaa funktiota siten, että se saa argumentikseen neliön sivun pituuden. Funktio näyttää siis tältä: ``piirra_nelio(sivun_pituus)``. Alla esimerkki funktiokutsusta, jolla voidaan piirtää erikokoisia neliöitä eri puolille piirtoikkunaa.

```python
import turtle

kyna = turtle.Turtle()

# Piirretään neliö, jonka sivun pituus on 50 kohtaan (-100, 0)
kyna.goto(-100, 0)
piirra_nelio(50)

# Piirretään neliö, jonka sivun pituus on 100 kohtaan (0, 100)
kyna.goto(0, 100)
piirra_nelio(100)

# Piirretään neliö, jonka sivun pituus on 150 kohtaan (200, 0)
kyna.goto(200, 0)
piirra_nelio(150)
```

# Tehtävä 2 - Ympyräfunktio

a) Luo funktio, joka piirtää ympyrän pisteeseen (x, y). x- ja y-koordinaatti annetaan funktiolle argumenttina. Esimerkki funktiokutsusta:

```python
piirra_ympyra(25, 120) # Piirtää ympyrän pisteeseen (25, 120)
```

b) Muokkaa funktiota siten, että se ottaa argumentikseen myös ympyrän säteen. Voit siis piirtää funktiolla erikokoisia ympyröitä eri puolille piirtoikkunaa.

```python
piirra_ympyra(25, 120, 3) # Piirtää ympyrän, jonka säde on 3 pisteeseen (25, 120)
piirra_ympyra(-25, -120, 50) # Piirtää ympyrän, jonka säde on 50 pisteeseen (-25, -120)
piirra_ympyra(180, -50, 14) # Piirtää ympyrän, jonka säde on 14 pisteeseen (180, -50)
```

c) Piirrä satunnaisenkokoisia ympyröitä satunnaisiin paikkoihin eri puolille piirtoikkunaa. Ympyrän koko voi vaihdella välillä 1 - 15.

# Tehtävä 3 - Väritysehto

a) Kysy käyttäjältä haluaako hän värittää ympyrän vai ei. Piirrä sen jälkeen ympyrä ja väritä se tai jätä värittämättä käyttäjän vastauksen perusteella.

b) Muokkaa ohjelmaa siten, että käyttäjä voi valita millä värillä ympyrä väritetään. Valittavana voi olla muutama väri, esim. punainen, vihreä ja sininen. Luonnollisesti, jos käyttäjä ei halua värittää ympyrää, värejä ei myöskään kysytä.

Esimerkki ohjelman suorituksesta. Kaikki kaksoispisteen jälkeiset tekstit ovat käyttäjän kirjoittamia. Molemmissa esimerkkisuorituksissa ohjelma piirtää ympyrän ja värittää sen annetulla värillä tai jättää värittämättä.

```
Tässä ohjelmassa voit halutessasi värittää ympyrän.
K värittää ja E jättää ympyrän värittämättä.
Valinta: K
Valitse väri. Kirjoita väri pienellä ja englanniksi.
Kirjoita väri englanniksi: green
```

```
Tässä ohjelmassa voit halutessasi värittää ympyrän.
K värittää ja E jättää ympyrän värittämättä.
Valinta: E
```

# Tehtävä 5 - Suomenkieliset värit

Kysy käyttäjältä väriä suomeksi. Piirrä sen jälkeen neliö ja väritä se käyttäjän syöttämällä värillä. Riittää, että ohjelma toimii kolmella värillä, esim. sininen, punainen ja vihreä. Jos käyttäjä kirjoittaa jonkin muun värin, ohjelma tulostaa tekstin "väriä ei tunnisteta". Kirjainten kokoa ei tarvitse huomioida, voit olettaa että käyttäjä käyttää pelkästään pieniä kirjaimia.

# Tehtävä 6 - Yksinkertainen käyttöliittymä

Toteuta yksinkertainen käyttöliittymä, jolla voit kysyä käyttäjältä miten hän haluaa kynää liikutettavan. Hyödynnetään tätä ohjelmaa myös myöhemmin. Tee kohdat vaihe-vaiheelta, niin saat sopivalla tavalla toimivan ohjelman.

a) Luo funktio ``tulosta_ohjeet()``, joka kertoo käyttäjälle miten ohjelma toimii. Esimerkkitulostus funktion toiminnasta:

```
Miten haluat, että piirtoalueella liikutaan?
Eteenpäin (1)
Taaksepäin (2)
Oikealle (3)
Vasemmalle (4)
Lopetus (5)
```

b) Kysy käyttäjältä valintaa niin kauan, kunnes hän syöttää luvun 5. Kun luku 5 syötetään, ohjelma tulostaa tekstin "Kiitos ja hei!" ja ohjelman suoritus päättyy. Esimerkkitulostus:

```
Miten haluat, että piirtoalueella liikutaan?
Eteenpäin (1)
Taaksepäin (2)
Oikealle (3)
Vasemmalle (4)
Lopetus (5)
Valintasi: 1
Valintasi: 1
Valintasi: 3
Valintasi: 5
Kiitos ja hei!
```

c) Huolehdi, että ainoastaan luvut 1-5 kelpaavat. Jos käyttäjä syöttää jonkin muun luvun, ohjelma tulostaa tekstin "Valinta ei kelpaa". Esimerkkitulostus:

```
Miten haluat, että piirtoalueella liikutaan?
Eteenpäin (1)
Taaksepäin (2)
Oikealle (3)
Vasemmalle (4)
Lopetus (5)
Valintasi: 1
Valintasi: 4
Valintasi: 1
Valintasi: 9
Valinta ei kelpaa
Valintasi: 5
Kiitos ja hei!
```

d) Tallenna käyttäjän syöttämät liikkeet listaan ja tulosta listan sisältö, kun käyttäjä lopettaa liikkeiden syöttämisen. Alla esimerkki, miten listaan voidaan lisätä alkioita.

```python
listan_nimi = [] # Luodaan tyhjä lista. Anna listalle sitä kuvaava nimi.
listan_nimi.append(2) # Lisätään listan loppuun luku 2
listan_nimi.append('ohjelmointi on kivaa') # Lisätään listan loppuun merkkijono "ohjelmointi on kivaa"
print(listan_nimi) # Tulostetaan listan sisältö
```

Esimerkkitulostus lopullisesta ohjelmasta. Kaikki kaksoispisteen jälkeiset numerot ovat käyttäjän kirjoittamia.

```
Miten haluat, että piirtoalueella liikutaan?
Eteenpäin (1)
Taaksepäin (2)
Oikealle (3)
Vasemmalle (4)
Lopetus (5)
Valintasi: 1
Valintasi: 1
Valintasi: 3
Valintasi: 2
Valintasi: 2
Valintasi: 4
Valintasi: 1
Valintasi: 9
Valinta ei kelpaa
Valintasi: 3
Valintasi: 1
Valintasi: 5
Kiitos ja hei!
Kynän liikkeet ovat:
['eteenpäin', 'eteenpäin', 'oikealle', 'taaksepäin', 'taaksepäin', 'vasemmalle', 'eteenpäin', 'oikealle', 'eteenpäin']    
```

# Tehtävä 7 - Yksinkertaisia pinta-aloja

a) Luo funktio ``laske_nelion_ala(sivu)``, joka ottaa argumentikseen neliön sivun pituuden ja palauttaa neliön pinta-alan. Esimerkki pääohjelmasta, jolla funktion tulee toimia.

```python
nelion_ala = laske_nelion_ala(20)
print(nelion_ala) # Tulostaa 400
```

b) Luo funktio ``laske_kolmion_ala(kanta, korkeus)``, joka ottaa argumentikseen kolmion kannan ja korkeuden ja palauttaa vastaavan kolmion pinta-alan. Esimerkki pääohjelmasta:

```python
kolmion_ala = laske_kolmion_ala(10, 5)
print(kolmion_ala) # Tulostaa 25
```

c) Luo funktio ``laske_ympyran_ala(sade)``, joka ottaa argumentikseen ympyrän säteen ja palauttaa vastaavan ympyrän pinta-alan. Tarvitset tässä piitä, saat sen esimerkiksi matikkakirjastosta komennolla ``math.pi`` Esimerkki pääohjelmasta:

```python
import math # Muista tämä alkuun!

ympyran_sade = 28
ympyran_ala = laske_ympyran_ala(ympyran_sade)
print(ympyran_ala) # Tulostaa 2463.0086404143976
```

d) Lisätehtävä: luo yksinkertainen pinta-alalaskuri, joka kysyy käyttäjältä minkä kuvion pinta-alan hän haluaa laskea. Kuvion perusteella kysytään lisätietoja kuviosta ja lasketaan ja tulostetaan oikea vastaus.

# Tehtävä 8 - Suorakulmainen kolmio

Huom! Toteutus kolmion piirtämiselle on tehty ensimmäisen tehtäväpaketin tehtävässä 7. Tässä muokataan aiempaa toteutusta hieman toisenlaiseksi, voit katsoa mallia aiemmasta jos haluat.

a) Luo funktio ``laske_hypotenuusa(a, b)``, joka ottaa argumenttina suorakulmaisen kolmion kateettien pituudet. Funktio laskee ja palauttaa suorakulmaisen kolmion hypotenuusan pituuden. Jos $a$ ja $b$ ovat kateetteja, hypotenuusa $$c = \sqrt(a^2 + b^2)$

Neliöjuuren voit laskea matikkakirjaston avulla:

```python
import math # Muista ottaa kirjasto käyttöön!
luku = 12
neliojuuri = math.sqrt(luku) # Laskee luvun 12 neliöjuuren ja tallentaa tuloksen muuttujaan
```

b) Luo funktio ``laske_kulma(a, b)``, joka laskee ja palauttaa suorakulmaisen kolmion toisen terävän kulman ulkokulman suuruuden. Ulkokulmaa tarvitaan, kun piirretään kolmio seuraavassa kohdassa. Ulkokulman suuruus lasketaan
$$\alpha = 180^\circ - \tan(a / b) \cdot 180 / \pi$$

Kulman tangentin ja piin arvon voit määrittää myös matikkakirjaston avulla:

```python
import math
tangentti = math.atan2(a, b) # Laskee tangentin luvulle a/b
pii = math.pi # Piin likiarvo
```

c) Täydennä alla oleva ohjelma siten, että se piirtää suorakulmaisen kolmion käyttäjän syöttämien kateettien perusteella.

```python
import math
import turtle

a = int(input('Anna ensimmäinen kateetti: '))
b = int(input('Anna toinen kateetti: '))

c = laske_hypotenuusa(a, b)
kulma = laske_kulma(a, b)

# Toteuta piirtäminen tähän
```

d) Luo funktio ``piirra_kolmio(a, b)``. Edellisen kohdan piirto pitää onnistua alla olevalla pääohjelmalla.

```python
import math
import turtle

a = int(input('Anna ensimmäinen kateetti: '))
b = int(input('Anna toinen kateetti: '))

piirra_kolmio(a, b)
```