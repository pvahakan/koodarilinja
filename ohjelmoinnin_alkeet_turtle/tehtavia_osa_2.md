# Tehtävä 1

Piirrä neliö käyttäen for-silmukkaa.

# Tehtävä 2

Piirrä säännöllinen kahdeksankulmio käyttäen for-silmukkaa. Voit laskea säännöllisen kahdeksankulmion kulman suuruuden paperilla.

# Tehtävä 3

Muokkaa tehtävää 2 siten, että kulma, sivujen määrä sekä sivun pituus luetaan muuttujasta. **Ohjelman tulee laskea kulma sivujen määrän perusteella**. Ohjelma toimii oikein, jos muutat **ainoastaan sivujen määrää** ja saat piirrettyä minkä tahansa säännöllisen monikulmion.

Monikulmion sisäkulman suuruus saadaan laskettua:

$$kulma = \frac{180 \cdot (n-2)}{n}$$, missä $n$ on kulmien lukumäärä.

Turtlessa tarvitaan kuitenkin ulkokulmaa, joka saadaan $180 - kulma$.

# Tehtävä 4

Muokkaa edellistä ohjelmaa siten, että sivujen määrä kysytään käyttäjältä. Ohjelman tulee piirtää säännöllinen monikulmio, jossa on käyttäjän syöttämä määrä sivuja.

# Tehtävä 5

Piirrä spiraali, jossa on 20 "sivua". Kasvata jokaisen käännöksen jälkeen piirrettävän viivan pituutta 10:llä. Aloita piirtäminen sivun pituudesta 10 ja käytä käännöskulmana 40 astetta. **Tarvitset tässä muuttujaa, joka sisältää piirrettävän sivun pituuden sekä for-silmukkaa**

# Tehtävä 6

Piirrä kolme kuviota eri kohtaan piirtoikkunaa. Väritä jokainen kuvio eri värillä. Kopioi seuraava rivi ohjelmaasi ja ota värit annetusta listasta.

```python
varit = ['salmon', 'moccasin', 'maroon']
```

# Tehtävä 7 - Kuuden viivan kuvio

Piirrä kuvio, jossa on kuusi viivaa. Jokainen viiva tulee olla eri värinen. Ota värit alla olevasta listasta. Muuta kynän kokoa hieman suuremmaksi, jotta näet viivan värin paremmin.

```python
varit = ['dark khaki', 'pale green', 'sandy brown', 'crimson', 'orchid', 'dark magenta']
```

# Tehtävä 8 - Värit listasta

Muokkaa edellinen ohjelma sellaiseksi, että värit luetaan listasta käyttäen for-silmukkaa. Suorita myös piirtäminen ja kääntäminen silmukan sisällä.

# Tehtävä 9 - Muuttuva sivun pituus

Muokkaa tehtävän 8 ohjelma sellaiseksi, että piirrettävän sivun pituus annetaan muuttujassa ja aluksi se on 10. Jokaisella kierroksella sivun pituuden tulee kasvaa kaksinkertaiseksi. Kulman voit päättää itse, mutta etsi kokeilemalla sellainen, että muodostunut spiraali mahtuu piirtoalueen sisään.

# Tehtävä 10 - Ruudunkokoinen spiraali

Piirrä spiraali käyttäen while-silmukkaa. Aseta aluksi viivan pituudeksi 10. Jatka spiraalin piirtämistä niin kauan, kun viivan pituus on 500. Käännä kynää silmukan sisällä 90 astetta ja kasvata viivan pituutta 20:llä.

Kokeile vaihtaa kulman ja viivan kasvattamisen arvoja. Kaikki yli 90 asteen kulmat pitäisi mahtua piirtoalueen sisään.

# Tehtävä 11 - Yksinkertainen lumisade

a) Piirrä "lumihiutale" satunnaiseen paikkaan piirtoalueella. Lumihiutale voi olla tässä ympyrä, jonka säde on 3.

Tarvitset tässä Pythonin random-kirjastoa. Esimerkki, miten voit liikuttaa kynää satunnaisesti eri paikkaan.

```python
import random # Lisää tämä koodin alkuun

# Luodaan satunnaiset koordinaatit.
# Sopivat ala- ja ylärajat voi etsiä kokeilemalla.
# -250 ja 250 pitäisi olla aika lähellä reunoja.
x = random.randint(-250, 250) # Satunnaisluku väliltä -250 - 250
y = random.randint(-250, 250)

kyna.goto(x, y) # Siirretään kynä pisteeseen (x, y)
```

b) Piirrä lumisade, jossa on 50 lumihiutaletta. Lumihiutale voi olla tässä ympyrä, jonka säde on esim. 3. Käytä tässä while-silmukkaa. Tarvitset myös muuttujan, joka laskee kuinka monta lumihiutaletta on jo piirretty.

**Huom. Piirtämisen nopeuttamiseksi aseta kynän nopeus suureksi ja piilota kynä.**

```python
kyna.speed(0)
kyna.hideturtle() # Tällä voit piilottaa kynän näkyvistä
```