#!/usr/bin/env python3


# Pseudokoodi siitä, miten peli tulisi rakentaa. Luodaan toteutus
# luokkien avulla tämän pohjalta.

# # Luodaan objektit
# solun_koko = 20
# solujen_maara = 20
# 
# kentta = Kentta()
# ruoka = Ruoka()
# snake = Snake()
# logiikka = Logiikka()
# 
# while running:
#     # Tarkistetaan käyttäjän syötteet
#     syote = Kayttoliittyma.hae_syotteet()
#     if syote == lopeta:
#         running = False
#         Kayttoliittyma.lopeta()
#     if syote == vasemmalle:
#         snake.liikuta_vasemmalle()
#     if syote == oikealle:
#         snake.liikuta_oikealle()
#     if syote == ylos:
#         snake.liikuta_ylos()
#     if syote == alas:
#         snake.liikuta_alas()
# 
#     # Päivitetään snaken sijainti
#     snake.paivita()
# 
#     # Tarkistetaan osuma seiniin, itseen tai ruokaan
#     osuma = logiikka.tarkista_osuma()
#     if osuma == None:
#         pass
#     elif osuma == reuna:
#         kayttoliittyma.lopeta()
#     elif osuma == snake:
#         kayttoliittyma.lopeta()
#     elif osuma == ruoka:
#         snake.kasvata()
#         snake.lisaa_piste()
#         ruoka.uusi_sijainti()
#     
#     # Piirretään elementit
#     kayttoliittyma.piirra_kentta()
#     kayttoliittyma.piirra_snake()
#     kayttoliittyma.piirra_ruoka()

from grid_game import Peli
from grid_game import Snake
from grid_game import Nappaimisto
from grid_game import Ruoka

import time

peli = Peli(25) # Luodaan pelikenttä, 25x25 -ruutua. Ruudun koko määräytyy Peli-luokassa.
mato = Snake(peli)
ruoka = Ruoka(peli)
nappaimisto = Nappaimisto()

syominen = False

# Hoidetaan nämä luokkien mato ja ruoka konstruktoreissa
# peli.lisaa_mato(mato) # Lisätään mato pelikentälle
# peli.lisaa_ruoka(ruoka) # Lisätään ruoka

if __name__ == '__main__':
    while peli.running:
        for tapahtuma in peli.hae_tapahtumat():
            # Pelin lopetuksen tarkistus
            if peli.tapahtuman_tyyppi(tapahtuma) == peli.sulje:
                peli.running = False

            if peli.tapahtuman_tyyppi(tapahtuma) == peli.paivitys:
                # Tähän lohkoon pitää laittaa kaikki päivittämiseen liittyvä, madon kasvattaminen, pistelasku yms.
                peli.paivita() # Päivitysfunktiossa huolehditaan madon liikuttamisesta. Ts. mato liikkuu automaattisesti, pitää huolehtia vain sen suunnasta.
                peli.tarkista_pelin_jatkuminen()
                syominen = peli.ruoka_syoty() # Uuden ruuan luonti voitaisiin siirtää pois tästä funktiosta
                if syominen == True:
                    mato.lisaa_pala()
                    mato.lisaa_piste()
                peli.piirra_kentta()

            # Tapahtumankäsittely aka. pelaajan kontrollit
            if peli.tapahtuman_tyyppi(tapahtuma) == nappaimisto.nappain_alas:
                if peli.hae_nappain(tapahtuma) == nappaimisto.alas:
                    if mato.suunta != mato.suunnat['ylös']:
                        mato.suunta = mato.suunnat['alas']
                if peli.hae_nappain(tapahtuma) == nappaimisto.ylos:
                    if mato.suunta != mato.suunnat['alas']:
                        mato.suunta = mato.suunnat['ylös']
                if peli.hae_nappain(tapahtuma) == nappaimisto.vasen:
                    if mato.suunta != mato.suunnat['oikea']:
                        mato.suunta = mato.suunnat['vasen']
                if peli.hae_nappain(tapahtuma) == nappaimisto.oikea:
                    if mato.suunta != mato.suunnat['vasen']:
                        mato.suunta = mato.suunnat['oikea']



    time.sleep(1)
    peli.lopeta()