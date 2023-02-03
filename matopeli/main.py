#!/usr/bin/env python3

import time

from grid_game import Peli
from grid_game import Snake
from grid_game import Nappaimisto
from grid_game import Ruoka

peli = Peli(25) # Luodaan pelikenttä, 25x25 -ruutua. Ruudun koko määräytyy Peli-luokassa.
mato = Snake(peli)
ruoka = Ruoka(peli)
nappaimisto = Nappaimisto()

syominen = False

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