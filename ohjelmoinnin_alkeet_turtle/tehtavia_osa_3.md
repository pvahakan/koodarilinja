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

# Tehtävä 3 - Lumihiutalefunktio

a) Edellisessä tehtävässä piirrettiin "lumihiutale" satunnaiseen paikkaan. Muodosta funktio ``piirra_lumihiutale(x, y)``, joka piirtää lumihiutaleen pisteeseen (x, y).

b) Muokkaa funktiota ``piirra_lumihiutale(x, y)`` siten, että kuvio näyttää hieman enemmän lumihiutaleelta.