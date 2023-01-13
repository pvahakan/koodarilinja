# Komentorivin käyttö

Komentorivi on yksi tärkeä työkalu ohjelmoinnissa. Normaalisti tietokonetta käytetään graafisen käyttöliittymän kautta, mutta komentorivi tarjoaa tekstipohjaisen käyttöliittymän tietokoneen käyttämiseksi. Seuraavien tehtävien avulla opetellaan hieman perusteita komentorivin käyttöä varten.

## Tehtävä 1

Avaa komentorivi joko ohjelmavalikosta (huom, komentorivistä käytetään myös nimityksiä terminaali tai pääte tai komentokehoite) tai painamalla Crtl + Alt + T. 

a) Kirjoita komentoriville komento ``ls`` ja paina Enter. Mitä näet?
b) Suorita komento ``ls -a``. Miten tulostus muuttuu a-kohtaan verrattuna?
c) Suorita komento ``ls -l``. Miten tulostus muuttuu?
d) Suorita komento ``ls -al``. Miten tulostus muuttuu c-kohtaan verrattuna?

### Selityksiä

Komento ``ls`` listaa nykyisen kansion sisällön. Nykyinen kansio näkyy komentorivillä ennen ``$``-merkkiä. Kun terminaali käynnistetään, oletushakemisto on käyttäjän kotihakemisto, jota merkitään ``~``-merkillä.

Viivalla erotettuja parametreja kutsutaan vivuiksi. Tehtävässä on esitetty pari yleistä vipua, joita käytetään ``ls``-komennon yhteydessä. Eri komennoilla on luonnollisesti erilaisia vipuja, vaikka usein ne ovat samankaltaisia.

Vipu ``-a`` näyttää myös piilotetut kansiot (pisteellä alkavat). ``-l`` puolestaa näyttää kansion sisältämistä tiedostoista enemmän tietoja, mm. muokkauspäivän, tiedoston koon sekä tietoja tiedoston omistus- ja suoritusoikeuksista.

## Tehtävä 2

Komennolla ``cd`` voi siirtyä komentorivillä hakemistosta toiseen (**c**hange **d**irectory). ``cd`` tarvitsee myös kohteen, jonne siirtyä. Esimerkiksi jos kotihakemistossa kirjoittaa ``cd Documents``, siirrytään terminaalissa kansioon ``Documents``. Voit todeta kansion vaihtuneen ``$``-merkkiä ennen olevasta kansiopolusta tai listaamalla kansion sisällön ``ls``-komennolla.

**Huom!** Komentorivi osaa täydentää kansioiden ja tiedostojen nimiä Tab-näppäimellä. Riittää, että kirjoitat esim. ``cd Doc`` ja painat Tab-näppäintä, niin kansion nimi täydentyy muotoon ``cd Documents``.

a) Listaa nykyisen kansion sisältö.
b) Siirry kansioon Asiakirjat ja listaa sen sisältö.
c) Suorita komento ``cd ..`` ja listaa kansion sisältö. Mitä tapahtui?
d) Siirry komentorivillä sellaiseen kansioon, johon olet tallentanut aiemmin tekemiäsi Python-ohjelmia. Listaa kansion sisältö näkyviin.
e) Suorita pelkästään komento ``cd`` (ilman tiedostopolkua). Listaa kansion sisältö. Mitä tapahtui?

**Huom!** Jos et ole varma missä kansiossa olet, komennolla ``pwd`` (**p**rint **w**orking **d**irectory) saat selville hakemistopolun jossa terminaali on.

## Tehtävä 3

``mkdir`` on komento, jolla voit luoda tyhjän kansion nykyisen kansion sisään. Komennolle annetaan lisäksi kansion nimi. Esimerkiksi ``mkdir ohjelmointi`` luo tyhjän kansion, jonka nimi on ohjelmointi.

a) Siirry komentorivillä kotihakemistoon jos et jo ole siellä.
b) Luo tyhjä kansio, jonka nimi on "komentoriviharjoittelua" ja siirry juuri luotuun kansioon.
c) Listaa kansion sisältö, jotta se on varmasti tyhjä.

## Tehtävä 4

Komentorivillä voidaan käyttää myös erilaisia ohjelmia, kuten tiettyjä tekstieditoreita. Yksi tekstieditori on nano.

a) Varmista komennolla ``pwd``, että olet kansiossa "komentoriviharjoittelua" (joka luotiin tehtävässä 3).
b) Suorita komento ``nano tekstitiedosto.txt``, joka avaa nano-editorilla tiedoston tekstitiedosto.txt (jos tiedostoa ei ole, se luodaan).
c) Kirjoita tiedostoon jotakin tekstiä. Tallenna (Crtl + o) ja sulje (Crtl + x) tiedosto.
d) Listaa hakemiston rakenne, niin näet että hakemistoon on ilmestynyt yksi tekstitiedosto.

## Tehtävä 5

a) Luo kansion "komentoriviharjoittelua" sisään uusi kansio, jonka nimi on "alikansio".
b) Luo alikansion sisään kaksi kansiota "koodit" ja "tekstit".
c) Luo kansioon "koodit" Python-tiedosto "hello.py" (käytä nanoa) joka sisältää yhden rivin koodia. Koodi tulostaa näytölle tekstin "Hello".
d) Luo kansioon "tekstit" tiedosto "tervehdys.txt" ja kirjoita sen sisään jokin tervehdys.

## Tehtävä 6

Komento ``tree`` näyttää hakemistorakenteen puukaaviona. Siirry kansioon "komentoriviharjoittelua" ja suorita siinä kansiossa komento ``tree``. Tulostuksen pitäisi näyttää viiden ensimmäisen tehtävän jälkeen seuraavalta.

```
.
|--koodit
|   |____ hello.py
|
|--tekstit
|   |____ tervehdys.txt
|
|__tiedosto_1.txt
```