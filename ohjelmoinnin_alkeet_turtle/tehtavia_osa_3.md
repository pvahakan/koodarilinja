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