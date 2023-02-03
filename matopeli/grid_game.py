import pygame
import random
from pygame.math import Vector2

class Snake:
    """
    Luokka, jota käytetään snaken toimintojen luomiseen.
    """

    def __init__(self, peli):
        """
        Parameters:
        -----------
        peli : Peli
            Peli-luokan objekti, johon mato kuuluu.

        Attributes
        ----------
        body : list
            Lista snaken palasten sijainneista. Sijainnit ovat tallennettu pygamen vector2-muodossa.
        suunta : pygame.math.Vector2
            Suunta, johon snake liikkuu. Oletuksena oikealle.
        uusi_pala : bool
            Muuttuja, jonka avulla selvitetään tarvitseeko snakelle luoda uusi pala vai ei.
        """

        self.peli = peli
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]
        self.suunnat = {'vasen' : Vector2(-1, 0), 'oikea' : Vector2(1, 0), 'ylös' : Vector2(0, -1), 'alas' : Vector2(0, 1)}
        self.suunta = self.suunnat['oikea']
        self.uusi_pala = False
        self.pisteet = 0
        self.peli.lisaa_mato(self)

    def lisaa_piste(self):
        """Lisää madolle yhden pisteen.
        """

        self.pisteet += 1

    def nayta_pisteet(self):
        """Piirtää madon pistemäärän näytölle.
        """

        font = pygame.font.SysFont("Times New Roman", 18)       
        self.peli.naytto.blit(font.render(str(self.pisteet), True, 'black'), (10, 10))

    def piirra_snake(self):
        """Piirtää snaken näytölle.

        Piirtämisessä huomioidaan kentän solurakenne. Snake voi saada vain tietyt
        paikat kentältä riippuen kentälle annetusta solun koosta, joka on globaali
        muuttuja.
        """

        for block in self.body:
            snake_rect = pygame.Rect(block.x * self.peli.solun_koko, block.y * self.peli.solun_koko, self.peli.solun_koko, self.peli.solun_koko)
            pygame.draw.rect(self.peli.naytto, (183,111,122), snake_rect)

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
    def __init__(self, peli):
        self.peli = peli
        self.x = random.randint(0, self.peli.sivun_pituus - 1)
        self.y = random.randint(0, self.peli.sivun_pituus - 1)
        self.paikka = Vector2(self.x, self.y)
        self.peli.lisaa_ruoka(self)

    def piirra_ruoka(self):
        ruoka_rect = pygame.Rect(self.paikka.x*self.peli.solun_koko, self.paikka.y*self.peli.solun_koko, self.peli.solun_koko, self.peli.solun_koko)
        pygame.draw.rect(self.peli.naytto, (126, 166, 124), ruoka_rect)

    def uusi_sijainti(self):
        self.x = random.randint(0, self.peli.sivun_pituus - 1)
        self.y = random.randint(0, self.peli.sivun_pituus - 1)
        self.paikka = Vector2(self.x, self.y)

        run = False

class Peli:
    """
    Luokan tarkoitus on paketoida kaikki pygamen hankalalta näyttävät toiminnot
    yksinkertaisempaan pakettiin.

    Peli koostuu ruudukosta ja mato pystyy liikkumaan aina yhden ruudun kerrallaan.

    ...

    Attributes
    ----------
    solun_koko : int
        Pelilaudan yhden ruudun koko pikseleinä.
    sivun_pituus : int
        Pelikentän sivun pituus ruutuina. Pelilauta on aina neliö.
    nayton_sivu : int
        Pelikentän sivun pituus pikseleinä.

    Methods
    -------
    piirra_kentta()
        Piirtää alustuksessa annetun kokoisen kentän näytölle.
    hae_tapahtumat()
        Hakee tapahtumat, jotka käyttäjä pelille antaa PyGamen eventtien avulla.
    paivita()
        Päivittää pelikentän.
    lopeta()
        Sulkee ikkunan.
    """

    def __init__(self, koko : int):
        """
        Parameters
        ----------
        koko : int
            Pelilaudan sivun pituus ruutujen määrässä laskettuna. Pelilauta on neliö.
        running : boolean
            Muuttuja, joka pitää kirjaa onko peli käynnissä vai ei.
        """

        pygame.init()
        self.solun_koko = 20
        self.sivun_pituus = koko
        nayton_sivu = self.solun_koko * self.sivun_pituus
        self.naytto = pygame.display.set_mode((nayton_sivu, nayton_sivu))
        self.kello = pygame.time.Clock()
        self.sulje = pygame.QUIT
        self.running = True
        self.snake = None
        self.ruoka = None
        self.paivitys = pygame.USEREVENT # Tapahtuma, joka tarkistaa pitääkö näyttö päivittää vai ei
        pygame.time.set_timer(self.paivitys, 150)

    def piirra_kentta(self):
        """Piirtää kentän näytölle. 
        
        Kentän koko annetaan Peli-luokan alustuksessa. Funktio huolehtii madon, pistemäärän ja
        ruuan piirtämisestä.
        """

        self.naytto.fill((175, 215, 70))
        if self.snake is not None:
            self.snake.piirra_snake()
            self.snake.nayta_pisteet()
        if self.ruoka is not None:
            self.ruoka.piirra_ruoka()

    def lisaa_mato(self, snake):
        """Lisää madon pelikentälle.

        Parameters:
        -----------
        snake : Snake
            Kentälle lisättävä Snake-objekti
        """

        self.snake = snake

    def lisaa_ruoka(self, ruoka):
        """Lisää ruuan pelikentälle

        Parameters:
        -----------
        ruoka : Ruoka
            Kentälle lisättävä Ruoka-objekti
        """

        self.ruoka = ruoka

    def hae_tapahtumat(self):
        """Hakee käyttäjän antamat reaktiot / syötteet PyGamen eventteinä.

        Returns
        -------
        list
            Lista tapahtumista PyGamen event -muodossa.
        """

        events = pygame.event.get()
        return [event for event in events]

    def tapahtuman_tyyppi(self, event):
        """Hakee tapahtuman tyypin.

        Parameters
        ----------
        event : kygame.event
            Tapahtuma, jonka tyyppiä selvitetään.

        Returns
        -------
        pygame.event.type
            Selvitettävän tapahtuman tyyppi.
        """

        return event.type

    def hae_nappain(self, tapahtuma):
        """Hakee näppäinpainalluksen näppäimen.

        Funktiossa oletetaan, että tapahtuma on tyyppiä pygame.KEYDOWN.

        Parameters
        ----------
        tapahtuma : pygame.event

        Returns
        -------
        pygame.event.key
            Selvitettävän näppäinpainalluksen näppäin.
        """

        return tapahtuma.key

    def paivita(self):
        """Päivittää pelikentän.

        Funktio huolehtii madon liikuttamisesta.
        """

        if self.snake is not None:
            self.snake.liikuta()

        pygame.display.flip()
        self.kello.tick(60)

    def tarkista_pelin_jatkuminen(self):
        """Tarkistaa päättyykö peli vai jatkuuko se.

        Funktio tutkii osuuko mato pelikentän reunoihin tai itseensä.
        Funktio muuttaa instanssimuuttujan running tilan Falseksi.
        """

        # Osuminen seiniin
        if not 0 <= self.snake.body[0].x <= self.sivun_pituus - 1:
            self.running = False
        if not 0 <= self.snake.body[0].y <= self.sivun_pituus - 1:
            self.running = False
        
        # Osuminen matoon
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.running = False

    def ruoka_syoty(self):
        """Tarkistaa osuuko mato ruokaan.

        Funktio luo ruualle uuden sijainnin.

        Returns:
        --------
        boolean
            Palauttaa True, jos mato osuu ruokaan. False muuten.
        """

        if self.ruoka.paikka == self.snake.body[0]:
            self.ruoka.uusi_sijainti()
            return True

        return False

    def lopeta(self):
        """Sulkee peli-ikkunan.
        """

        self.running = False
        pygame.quit()

class Nappaimisto:
    """Luokka näppäimistöpalautteen käsittelyyn.
    """

    def __init__(self):
        self.vasen = pygame.K_LEFT
        self.oikea = pygame.K_RIGHT
        self.ylos = pygame.K_UP
        self.alas = pygame.K_DOWN
        self.nappain_alas = pygame.KEYDOWN
        self.nappain_ylos = pygame.KEYDOWN

if __name__ == '__main__':
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