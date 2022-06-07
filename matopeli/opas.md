# Ohjelmoinnin aloittaminen

Tietokone on tyhmä laite. Sille pitää kertoa, mitä sen täytyy tehdä. Tietokone ei osaa tehdä muuta, kuin mitä sen on käsketty tekemään, mutta nämä tehtävät se tekee nopeasti ja luotettavasti. Ihmisen tehtävä on kertoa, mitä koneen täytyy tehdä. Tätä kutsutaan ohjelmoinniksi.

Tällä sivulla opetellaan ohjelmoinnin perusteita Python-ohjelmointikielellä. Varsinainen ohjelma kirjoitetaan puhtaana tekstinä jollakin tekstieditorilla (esim. notepad, Visual Studio Code), ei kuitenkaan tekstinkäsittelyohjelmalla (Word). Python-kielen tapauksessa kirjoitettu ohjelmakoodi suoritetaan erillisen Python-tulkin avulla, joka kääntää ohjelmaa rivi riviltä tietokoneen ymmärtämään muotoon. Ohjelmoinnin opetteluun sopii hyvin Python-tulkin mukana tuleva Idle-ohjelmisto. Idle pitäisi löytyä opiskelijakoneelta valmiiksi asennettuna. Suurempiin projekteihin kannattanee käyttää jotakin hieman kehittyneempää tekstieditoria, kuten edellä mainittu Visual Studio Code.

## Tulostaminen ja syötteen kysyminen

Tietokoneohjelmat koostuvat erilaisista komennoista, joita ohjelmakoodiin kirjoitetaan. Tietokone suorittaa ohjelmoijan kirjoittamia komentoja peräjälkeen, minkä seurauksena saadaan toimiva ohjelma. Yksinkertaisia Pythonissa olevia komentoja ovat esimerkiksi ``print``, joka tulostaa asioita näytölle. ``input``-komennolla voidaan puolestaan pyytää käyttäjää antamaan jotakin tietoja (syöte) ohjelmalle.

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
