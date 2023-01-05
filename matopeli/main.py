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