# Ohjelmoinnin aloittaminen

Tietokone on tyhmä laite. Sille pitää kertoa, mitä sen täytyy tehdä. Tietokone ei osaa tehdä muuta, kuin mitä sen on käsketty tekemään, mutta nämä tehtävät se tekee nopeasti ja luotettavasti. Ihmisen tehtävä on kertoa, mitä koneen täytyy tehdä. Tätä kutsutaan ohjelmoinniksi.

Tällä sivulla opetellaan ohjelmoinnin perusteita Python-ohjelmointikielellä. Varsinainen ohjelma kirjoitetaan puhtaana tekstinä jollakin tekstieditorilla (esim. notepad, Visual Studio Code), ei kuitenkaan tekstinkäsittelyohjelmalla (Word). Python-kielen tapauksessa kirjoitettu ohjelmakoodi suoritetaan erillisen Python-tulkin avulla, joka kääntää ohjelmaa rivi riviltä tietokoneen ymmärtämään muotoon. Ohjelmoinnin opetteluun sopii hyvin Python-tulkin mukana tuleva Idle-ohjelmisto. Idle pitäisi löytyä opiskelijakoneelta valmiiksi asennettuna. Suurempiin projekteihin kannattanee käyttää jotakin hieman kehittyneempää tekstieditoria, kuten edellä mainittu Visual Studio Code.

## Tulostaminen

Tietokoneohjelmat koostuvat erilaisista komennoista, joita ohjelmakoodiin kirjoitetaan. Tietokone suorittaa ohjelmoijan kirjoittamia komentoja peräjälkeen, minkä seurauksena saadaan toimiva ohjelma. Yksinkertaisia Pythonissa olevia komentoja ovat esimerkiksi ``print``, joka tulostaa asioita näytölle.

## Esimerkki

Seuraava komento tulostaa tekstin "hei" näytölle.

```python
print('hei')
``` 

Komento on oltava juuri samalla tavalla, jotta Python-tulkki ymmärtää mitä me haluamme tehdä. Jos esimerkiksi yritämme suorittaa komennon

```python
print(hei)
```

seurauksena on virheilmoitus. Komento ei toimi, koska ``hei`` ei ole määritelty merkkijonoksi ja Python-tulkki ei ymmärrä sen olevan tekstiä. Merkkijonot pitää laittaa lainausmerkkien tai heittomerkkien sisään: ``'hei'`` ja ``"hei"`` käsitellään merkkijonona.

Ohjelmat koostuvat useista komennoista. Komennot suoritetaan järjestyksessä ylhäältä alaspäin. Esimerkiksi ohjelma 

```python
print('moi')
print('mitä')
print('kuuluu')
```

tulostaa sanat "moi", "mitä" ja "kuuluu" näytölle allekkain tässä järjestyksessä.

## Laskutoimitukset

Pythonia voidaan käyttää myös laskimena. Jos ``print``-komennon sisään laitetaan laskutoimitus, ohjelma tulostaa näytölle laskun vastauksen.

```python
print(2 + 2)
print(3 * 3)
print(2 + 3 * 5)
```

tulostaisi näytölle

```
4
9
17
```

Huomaa, että nyt numeroiden ympärillä ei ole lainausmerkkejä, koska ne ovat numeroita eikä merkkijonoja. Jos numeroiden ympärille laitetaan lainausmerkit, tilanne muuttuu merkittävästi.

```python
print(2 + 2 * 10)
print('2 + 2 * 10')
```

Yllä olevat komennot tulostuvat näytölle muodossa

```
12
2 + 2 * 10
```

Toisessa komennossa kyse on merkkijonosta, joten se tulostetaan merkki kerrallaan näytölle. Merkkijono tulostetaan siis sellaisenaan riippumatta sen sisällöstä.

## Kommentit

Kommentit ovat tärkeä osa ohjelman toimintaa. Jos rivin alussa on ``#``, kyseinen rivi käsitellään kommenttina eikä sen sisältö vaikuta ohjelman suoritukseen. **Kommentteja kannattaa käyttää riittävän paljon**, jotta ohjelman toimintaa olisi mahdollisimman helppo ymmärtää.

```python
print('Vuodessa on tunteja')
print(365 * 24) # 365 päivää ja päivässä 24 h
```

## Muuttujat

Muuttujat ovat hyvin tärkeitä ohjelmoinnissa. Ne ovat eräänlaisia tiedon talletuspaikkoja. Muuttujaan voidaan siis tallentaa jotakin tietoa ja tallennettua tietoa voidaan hyödyntää myöhemmin ohjelmassa. Ohjelmoija antaa itse muuttujille nimet. Nimeämisessä kannattaa suosia sellaista tapaa, että muuttujan nimestä näkee mitä se pitää sisällään. Matematiikassa ollaan totuttu käyttämään muuttujana kirjainta ``x``, mutta ohjelmoinnissa muuttuja ``pelaajan_nopeus`` on huomattavasti kuvaavampi kuin ``x``.

## Esimerkki

```python
nimi = 'Koodari' # Tallennetaan muuttujaan nimi merkkijono 'Koodari'
luku_1 = 10 # Tallennetaan muuttujaan luku_1 kokonaisluku 10
luku_2 = 20 # Tallennetaan muuttujaan luku_2 kokonaisluku 20
print(nimi) # Tulostetaan muuttujan nimi sisältämä arvo
print(luku_1 + luku_2) # Tulostetaan lukujen 1 ja 2 summa
```

Tulostus:

```
Koodari
30
```

***

Muuttujan arvoa voi myös muuttaa kesken ohjelman. Tämä on usein hyvin hyödyllistä, koska jokaiselle uudelle arvolle ei tarvitse keksiä uutta muuttujan nimeä.

## Esimerkki

```python
luku_1 = 10
print(luku_1)
luku_1 = 35
print(luku_1)
```

Tulostus

```
10
35
```
 
## Tiedon kysyminen käyttäjältä

Usein ohjelmien suorittamisessa tarvitaan tietoa käyttäjältä. Ohjelma voi tarvita esimerkiksi tiedon, mikä on henkilön nimi. Pythonissa tietoa voidaan kysyä ``input``-komennolla. Useimmiten ohjelmoinnissa puhutaan käyttäjän antamasta **syötteestä**. Syötteellä tarkoitetaan jotakin, mitä käyttäjä on syöttänyt ohjelmalle.

``input``-komennolle voi antaa merkkijonon, joka tulostuu näytölle. Sillä voi siis antaa ohjeen käyttäjälle, mitä hänen tulee syöttää ohjelmalle.

Jotta käyttäjän syötettä voidaan hyödyntää ohjelmassa myöhemmin, tulee syöte tallentaa johonkin muuttujaan. Jälleen kannattaa muuttujan nimeämisessä käyttää kuvaavaa nimeä.

## Esimerkki

```python
nimi = input('Kirjoita nimesi: ')
print(nimi)
```

Tulostus:

```
Kirjoita nimesi: Koodari
Koodari
```

Yllä olevassa tulostuksessa sana Koodari on käyttäjän kirjoittama ohjelman suorituksen aikana.

## Yhteenveto

- ``print()``-komennolla voidaan tulostaa näytölle esimerkiksi tekstiä tai numeroita.
- ``input()``-komennolla voidaan kysyä käyttäjältä syötettä.
- Muuttujaan tallennetaan tietoa, jota käytetään ohjelmassa. ``muuttujan_nimi = muuttujan_arvo``
- Muuttujien nimeämisessä kannattaa käyttää kuvaavia nimiä.
- ``'moikkamoi'`` ja ``'23'`` ovat merkkijonoja, eli tekstiä. Merkkijono määritellään lainausmerkeillä.
- ``5`` on numero, koska sen ympärillä ei ole lainausmerkkejä. Numeroilla voidaan tehdä laskutoimituksia.