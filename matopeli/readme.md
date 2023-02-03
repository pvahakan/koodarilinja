# Matopelin kuvaus

Matopeli toimii normaalin matopelin tavoin. Matoa liikutetaan ja pyritään syömään ruokaa. Ruoka kasvattaa matoa ja pelaajan pisteitä. Jos pelaaja osuu reunaan tai matoon itseensä, peli päättyy.

Tarkoitus on saada toimiva peli. Koodi tulee kirjoittaa sellaiseksi, että siinä on valmiit rakennuspalikat, joilla matopelin logiikka saadaan toimimaan suht yksinkertaisesti ilman turhaa PyGamen kanssa säätöä. Tämän projektin tarkoitus on opettaa ohjelmoinnin perusteita ja algoritmista ajattelua pelillisessä muodossa.

# Pelin rakentaminen

## Pelin tapahtumat

Peli koostuu useammasta tapahtumasta, joissa tilanteet käsitellään omalla tavallaan.

**Pelin päättyminen**

Jos pelin tapahtuma on pelin päättyminen, täytyy peli luonnollisesti lopettaa.

**Päivitys**

Päivitys-tapahtumassa pitää huolehtia monesta asiasta, jotta peli rullaa eteenpäin. Pelin logiikka täytyy päivittää yleisellä tasolla käyttäen Peli-luokan metodia ``Peli.paivita()``. Käytännössä tämä huolehtii siitä, että mato liikkuu eteenpäin koko ajan.

Tämän lisäksi päivitys-tapahtumassa täytyy tutkia jatkuuko peli vai ei. Jos ei jatku, niin sitten pelin täytyy loppua.

Päivitys-tapahtumassa tarkistetaan myös onko mato syönyt vai ei. Jos mato syö, täytyy madon kokoa sekä pistemäärää kasvattaa. Jos syömistä ei tapahdu, näitä ei luonnollisesti tehdä.

Lisäksi päivitys-tapahtumassa pitää vielä piirtää peli näkyviin. Piirtäminen täytyy tehdä vasta sen jälkeen, kun kaikki päivitykset on tehty.

**Näppäimen painallus**

Kolmas tapahtuma on näppäinten painallus. Tässä tapahtumassa täytyy tutkia mitä näppäintä on painettu ja toteuttaa toiminnot sen mukaan.

Tässä tapahtumassa on kaksi eri vaihetta. Ensin täytyy tutkia onko tapahtuma näppäimen painallus alas. Jos tapahtuma on näppäimen painallus, täytyy selvittää mitä näppäintä on painettu ja toimia sen mukaan. Esim. jos painettu näppäin on ylänuoli, täytyy madon suunta muuttaa siten että se liikkuu ylös.

## Rakentaminen

Rakentaminen koostuu useammista vaiheista:

1. Luo pelikenttä ja toteuta pelin loppuminen rastia painamalla.
2. Lisää pelikentälle mato.
3. Toteuta madon liikkuminen nuolinäppäimillä.