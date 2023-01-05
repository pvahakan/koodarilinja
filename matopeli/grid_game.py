import pygame
import random
from pygame.math import Vector2

class Snake:
    """
    Luokka, jota käytetään snaken toimintojen luomiseen.
    """

    def __init__(self):
        """
        Parameters
        ----------
        body : list
            Lista snaken palasten sijainneista. Sijainnit ovat tallennettu pygamen vector2-muodossa.
        suunta : pygame.math.Vector2
            Suunta, johon snake liikkuu. Oletuksena oikealle.
        uusi_pala : bool
            Muuttuja, jonka avulla selvitetään tarvitseeko snakelle luoda uusi pala vai ei.
        """

        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]
        self.suunta = Vector2(1, 0)
        self.uusi_pala = False

    def piirra_snake(self):
        """Piirtää snaken näytölle.

        Piirtämisessä huomioidaan kentän solurakenne. Snake voi saada vain tietyt
        paikat kentältä riippuen kentälle annetusta solun koosta, joka on globaali
        muuttuja.
        """

        for block in self.body:
            snake_rect = pygame.Rect(block.x * solun_koko, block.y * solun_koko, solun_koko, solun_koko)
            pygame.draw.rect(naytto, (183,111,122), snake_rect)

    def liikuta(self):
        """Liikuttaa snakea haluttuun suuntaan.
        
        Luodaan kopio kaikista snaken palasista poislukien viimeinen. Kopion ensimmäiseksi
        elementiksi lisätään ensimmäinen elementti, johon on lisätty snaken suunta.
        Jos snakea täytyy kasvattaa, niin kopio luodaan kaikista aiemmista snaken palasista.
        """

        if self.uusi_pala == True:
            body_copy = self.body
            body_copy.insert(0, body_copy[0] + self.suunta) # Lisätään alkuun uusi elementti
            self.body = body_copy
            self.uusi_pala = False
        else:
            body_copy = self.body[:-1] # Poistetaan viimeinen elementti
            body_copy.insert(0, body_copy[0] + self.suunta) # Lisätään alkuun uusi elementti
            self.body = body_copy

    def lisaa_pala(self):
        """Funktio, jolla käsitellään palan lisäämisen tarve snakelle.

        """

        self.uusi_pala = True


class Ruoka:
    def __init__(self):
        self.x = random.randint(0, solujen_maara - 1)
        self.y = random.randint(0, solujen_maara - 1)
        self.paikka = Vector2(self.x, self.y)

    def piirra_ruoka(self):
        ruoka_rect = pygame.Rect(self.paikka.x*solun_koko, self.paikka.y*solun_koko, solun_koko, solun_koko)
        pygame.draw.rect(naytto, (126, 166, 124), ruoka_rect)

    def uusi_sijainti(self):
        self.x = random.randint(0, solujen_maara - 1)
        self.y = random.randint(0, solujen_maara - 1)
        self.paikka = Vector2(self.x, self.y)

"""
Yksinkertainen matopeli, logiikka toteutettu tutoriaalin https://www.youtube.com/watch?v=QFvqStqPCRU
perusteella.
"""
class Main:
    def __init__(self):
        self.snake = Snake()
        self.ruoka = Ruoka()
    
    def paivita(self):
        self.snake.liikuta()
        self.tarkista_osuma()
        self.tarkista_pelin_jatkuminen()

    def piirra_objektit(self):
        self.ruoka.piirra_ruoka()
        self.snake.piirra_snake()

    def tarkista_osuma(self):
        if self.ruoka.paikka == self.snake.body[0]:
            self.ruoka.uusi_sijainti()
            self.snake.lisaa_pala()

    def tarkista_pelin_jatkuminen(self):
        if not 0 <= self.snake.body[0].x <= solujen_maara - 1:
            self.game_over()
        if not 0 <= self.snake.body[0].y <= solujen_maara - 1:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        global run
        run = False

class Peli:
    """
    Luokan tarkoitus on paketoida kaikki pygamen hankalalta näyttävät toiminnot
    yksinkertaisempaan pakettiin.
    """

    def __init__(self, koko : int):
        """
        Parameters
        ----------
        koko : int
            Pelilaudan sivun pituus ruutujen määrässä laskettuna. Pelilauta on neliö.
        """

        pygame.init()
        self.solun_koko = 20
        self.sivun_pituus = koko
        nayton_sivu = self.solun_koko * self.sivun_pituus
        self.naytto = pygame.display.set_mode((nayton_sivu, nayton_sivu))
        self.kello = pygame.time.Clock()
        self.sulje = pygame.QUIT
        self.running = True

    def piirra_kentta(self):
        self.naytto.fill((175, 215, 70))

    def hae_tapahtumat(self):
        events = pygame.event.get()
        return [event.type for event in events]

    def paivita(self):
        pygame.display.flip()
        self.kello.tick(60)

    def lopeta(self):
        self.running = False
        pygame.quit()


# Alustetaan pelilauta
pygame.init()
solun_koko = 20
solujen_maara = 20
naytto = pygame.display.set_mode((solun_koko * solujen_maara, solun_koko * solujen_maara))
kello = pygame.time.Clock()

peli = Main()
run = True

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

if __name__ == '__main__':
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == SCREEN_UPDATE:
                peli.paivita()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if peli.snake.suunta.y != 1:
                        peli.snake.suunta = Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    if peli.snake.suunta.y != -1:
                        peli.snake.suunta = Vector2(0, 1)
                if event.key == pygame.K_LEFT:
                    if peli.snake.suunta.x != 1:
                        peli.snake.suunta = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT:
                    if peli.snake.suunta.x != -1:
                        peli.snake.suunta = Vector2(1, 0)

        naytto.fill((175, 215, 70))
        peli.piirra_objektit()
        pygame.display.flip()
        kello.tick(60)

    pygame.quit()