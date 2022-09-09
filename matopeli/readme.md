# Matopelin kuvaus

Matopeli toimii normaalin matopelin tavoin. Matoa liikutetaan ja pyritään syömään ruokaa. Ruoka kasvattaa matoa ja pelaajan pisteitä. Jos pelaaja osuu reunaan tai matoon itseensä, peli päättyy.

Tarkoitus on saada toimiva peli. Koodi tulee kirjoittaa sellaiseksi, että siinä on valmiit rakennuspalikat, joilla matopelin logiikka saadaan toimimaan suht yksinkertaisesti ilman turhaa PyGamen kanssa säätöä. Tämän projektin tarkoitus on opettaa ohjelmoinnin perusteita pelillisessä muodossa.

## Ominaisuudet

- [X] Matoa liikutetaan nuolilla
- [X] Ruokaa voi syödä
- [X] Ruoka kasvattaa pisteitä
- [X] Ruokaa tulee koko ajan lisää
- [ ] Mato kasvaa syödessä
- [X] Peli päättyy, kun osutaan reunoihin
- [ ] Peli päättyy, kun mato osuu itseensä

## Mitä opiskelijan halutaan tekevän?

Peli voitaisiin toteuttaa useammassa vaiheessa. Vaiheet yhdistämällä saataisiin valmis pelattava peli.

### Vaihe 1

Luo tietyn kokoinen ikkuna, johon peliä lähdetään rakentamaan. Tee ikkunasta myös sellainen, että se pysyy näkyvissä ja sulkeutuu, kun hiirellä klikataan rastia.

```python
leveys = 800
korkeus = 600

kaynnissa = True

ikkuna = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption('MATOPELI')

while kaynnissa:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            kaynnissa = False
```

### Vaihe 2

Tehtävänä on piirtää madon pää näkyviin edellisessä vaiheessa luotuun ikkunaan. Oletuksena madon pää piirretään kohtaan (200, 200). Päätä ei tarvitse vielä voida liikuttaa.

```python
leveys = 800
korkeus = 600

kaynnissa = True

ikkuna = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption('MATOPELI')

kello = pygame.time.Clock()

mato = Mato(2)

while kaynnissa:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            kaynnissa = False

    # Päivitetään pelilogiikka
    mato.paivita()

    # Piirretään kaikki tarvittava
    ikkuna.fill((0, 0, 0))
    mato.piirra(ikkuna)

    # Päivitetään PyGame:n ikkuna
    pygame.display.flip()
    kello.tick(60)
```

### Vaihe 3

Seuraavaksi tehtävänä on saada mato liikkumaan. Kontrolleina käytetään nuolinäppäimiä.

```python
leveys = 800
korkeus = 600

kaynnissa = True

ikkuna = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption('MATOPELI')

kello = pygame.time.Clock()

mato = Mato(2)

kontrollitarkistin = Kontrollit()

while kaynnissa:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            kaynnissa = False

        # Tarkistetaan, mitä painetaan
        kontrollit = kontrollitarkistin.tarkista_nappain(tapahtuma)

    # Liikutetaan matoa niin kauan kunnes
    # painetaan jotakin muuta nappia
    if kontrollit['alas']:
        mato.liiku_alas()
    elif kontrollit['ylös']:
        mato.liiku_ylos()
    elif kontrollit['vasemmalle']:
        mato.liiku_vasemmalle()
    elif kontrollit['oikealle']:
        mato.liiku_oikealle()

    # Päivitetään pelilogiikka
    mato.paivita()

    # Piirretään kaikki tarvittava
    ikkuna.fill((0, 0, 0))
    mato.piirra(ikkuna)

    # Päivitetään PyGame:n ikkuna
    pygame.display.flip()
    kello.tick(60)
```

### Vaihe 4

Seuraavassa vaiheessa lisätään peliin ruokaa sekä pistelasku. Tehtävänä on piirtää näytölle ruokaa ja tarkistaa, onko mato syönyt sen. Jos ruoka on syöty, tehdään lisää ruokaa ja madon pisteluku kasvaa. Madon ei tarvitse kasvaa vielä tässä vaiheessa.

```python
leveys = 800
korkeus = 600

kaynnissa = True

ikkuna = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption('MATOPELI')

kello = pygame.time.Clock()

mato = Mato(2)
omena = Ruoka(ikkuna)

kontrollitarkistin = Kontrollit()

while kaynnissa:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            kaynnissa = False

        # Tarkistetaan, mitä painetaan
        kontrollit = kontrollitarkistin.tarkista_nappain(tapahtuma)

    # Liikutetaan matoa niin kauan kunnes
    # painetaan jotakin muuta nappia
    if kontrollit['alas']:
        mato.liiku_alas()
    elif kontrollit['ylös']:
        mato.liiku_ylos()
    elif kontrollit['vasemmalle']:
        mato.liiku_vasemmalle()
    elif kontrollit['oikealle']:
        mato.liiku_oikealle()

    # Päivitetään pelilogiikka
    mato.paivita()
    if omena.on_syoty(mato):
        mato.lisaa_piste()
        omena = Ruoka(ikkuna)
        print(mato.pisteet)

    # Piirretään kaikki tarvittava
    ikkuna.fill((0, 0, 0))
    mato.piirra(ikkuna)
    omena.piirra(ikkuna)

    # Päivitetään PyGame:n ikkuna
    pygame.display.flip()
    kello.tick(60)
```

### Vaihe 5

Tässä vaiheessa lisätään madon törmäys seinään. Muokkaa ohjelmaa siis siten, että peli päättyy, kun mato osuu seinään.

```python
leveys = 800
korkeus = 600

kaynnissa = True

ikkuna = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption('MATOPELI')

kello = pygame.time.Clock()

mato = Mato(2)
omena = Ruoka(ikkuna)

kontrollitarkistin = Kontrollit()

while kaynnissa:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            kaynnissa = False

        # Tarkistetaan, mitä painetaan
        kontrollit = kontrollitarkistin.tarkista_nappain(tapahtuma)

    # Liikutetaan matoa niin kauan kunnes
    # painetaan jotakin muuta nappia
    if kontrollit['alas']:
        mato.liiku_alas()
    elif kontrollit['ylös']:
        mato.liiku_ylos()
    elif kontrollit['vasemmalle']:
        mato.liiku_vasemmalle()
    elif kontrollit['oikealle']:
        mato.liiku_oikealle()

    # Päivitetään pelilogiikka
    mato.paivita()
    if omena.on_syoty(mato):
        mato.lisaa_piste()
        omena = Ruoka(ikkuna)
        print(mato.pisteet)
    if mato.tormaa_seinaan():
        kaynnissa = False

    # Piirretään kaikki tarvittava
    ikkuna.fill((0, 0, 0))
    mato.piirra(ikkuna)
    omena.piirra(ikkuna)

    # Päivitetään PyGame:n ikkuna
    pygame.display.flip()
    kello.tick(60)
```