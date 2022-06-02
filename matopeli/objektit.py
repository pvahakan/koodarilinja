import pygame

pygame.init()

class Mato(pygame.sprite.Sprite):
    def __init__(self, nopeus : int):
        super().__init__()
        self.nopeus = nopeus

        self.paa = pygame.sprite.GroupSingle()
        self.hanta = pygame.sprite.Group()

        self.paa.add(MatoObjekti(200, 200))

    def liiku_alas(self):
        for paa in self.paa:
            paa.rect.y += self.nopeus

    def liiku_ylos(self):
        for paa in self.paa:
            paa.rect.y -= self.nopeus

    def liiku_vasemmalle(self):
        for paa in self.paa:
            paa.rect.x -= self.nopeus

    def liiku_oikealle(self):
        for paa in self.paa:
            paa.rect.x += self.nopeus

    def paivita(self):
        self.paa.update()
        self.hanta.update()

    def piirra(self, ikkuna):
        self.paa.draw(ikkuna)

class MatoObjekti(pygame.sprite.Sprite):
    '''
    Madon rakennuspalikka. Palikoita lisäämällä
    muodostetaan pää ja häntä.
    '''
    def __init__(self, x : int, y : int):
        super().__init__()

        self._sivu = 10 # Neliön sivun pituus
        self.color = 'blue'

        # Aloituspaikka
        self.x = x
        self.y = y
        self.image = pygame.Surface([self._sivu, self._sivu])
        pygame.draw.rect(self.image, 'gray', [0, 0, 10, 10])
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y

        # pygame.draw.circle(self.image, self.color, (self.x, self.y), self._sivu / 2)

class Kontrollit:
    def __init__(self):
        self.kontrollit = {'alas' : False,
                            'ylös' : False,
                            'vasemmalle' : False,
                            'oikealle' : False}

    def alusta_kontrollit(self):
        self.kontrollit = {'alas' : False,
                            'ylös' : False,
                            'vasemmalle' : False,
                            'oikealle' : False}


if __name__ == '__main__':
    leveys = 800
    korkeus = 600

    kaynnissa = True

    ikkuna = pygame.display.set_mode((leveys, korkeus))
    pygame.display.set_caption('MATOPELI')

    kello = pygame.time.Clock()

    mato = Mato(2)

    ylos, alas, oikealle, vasemmalle = False, False, False, False

    while kaynnissa:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                kaynnissa = False

            # Tarkistetaan, mitä painetaan
            # Tallennetaan tieto muuttujaan
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_DOWN:
                    ylos, vasemmalle, oikealle = False, False, False
                    alas = True
                elif tapahtuma.key == pygame.K_UP:
                    alas, vasemmalle, oikealle = False, False, False
                    ylos = True
                elif tapahtuma.key == pygame.K_LEFT:
                    alas, ylos, oikealle = False, False, False
                    vasemmalle = True
                elif tapahtuma.key == pygame.K_RIGHT:
                    alas, vasemmalle, ylos = False, False, False
                    oikealle = True

        # Liikutetaan matoa niin kauan kunnes
        # painetaan jotakin muuta nappia
        if alas:
            mato.liiku_alas()
        elif ylos:
            mato.liiku_ylos()
        elif vasemmalle:
            mato.liiku_vasemmalle()
        elif oikealle:
            mato.liiku_oikealle()

        # Päivitetään pelilogiikka
        mato.paivita()

        # Piirretään kaikki tarvittava
        ikkuna.fill((0, 0, 0))
        mato.piirra(ikkuna)

        # Päivitetään PyGame:n ikkuna
        pygame.display.flip()
        kello.tick(60)






# class Reuna(pygame.sprite.Sprite):
#     def __init__(self, leveys : int, korkeus : int):
#         super().__init__()
#         self.image = pygame.Surface([leveys, korkeus])
#         pygame.draw.rect(self.image, 'gray', [0, 0, leveys, korkeus])
#         self.rect = self.image.get_rect()
# 
#     def siirra(self, x, y):
#         self.rect.x = x
#         self.rect.y = y
# 
# class Mato(pygame.sprite.Sprite):
#     def __init__(self, leveys : int, korkeus : int):
#         super().__init__()
#         self.image = pygame.Surface([leveys, korkeus])
#         pygame.draw.rect(self.image, 'blue', [0, 0, leveys, korkeus])
# 
#         self.rect = self.image.get_rect()
#         self.hanta = []
#         self.pisteet = 0
# 
#     def siirra_vasemmalle(self, pikselit):
#         self.rect.x -= pikselit
#         self.suunta = 'vasen'
# 
#     def siirra_oikealle(self, pikselit):
#         self.rect.x += pikselit
#         self.suunta = 'oikea'
# 
#     def siirra_alas(self, pikselit):
#         self.rect.y += pikselit
#         self.suunta = 'alas'
# 
#     def siirra_ylos(self, pikselit):
#         self.rect.y -= pikselit
#         self.suunta = 'ylös'
# 
#     def syo(self, ruoka : pygame.sprite.GroupSingle):
#         tulos = pygame.sprite.spritecollide(self, ruoka, True)
#         return tulos
# 
#     def lisaa_piste(self):
#         self.pisteet += 1
#         print(self.pisteet)
# 
#     def tormaa(self, reuna : pygame.sprite.Sprite):
#         return pygame.sprite.collide_rect(self, reuna)
# 
# class HannanOsa(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.Surface([8, 8])
#         pygame.draw.rect(self.image, 'blue', [0, 0, 8, 8])
#         self.rect = self.image.get_rect()
# 
#     def siirra(self, x : int, y : int):
#         self.rect.x = x
#         self.rect.y = y
# 
# class Hanta():
#     def __init__(self, mato : Mato):
#         self.hanta = pygame.sprite.Group()
#         self.mato = mato
#         self.koordinaatit = []
# 
#     def siirra_hantaa(self):
#         self.koordinaatit.append((self.mato.rect.x, self.mato.rect.y))
#         if len(self.koordinaatit) > self.mato.pisteet:
#             del(self.koordinaatit[0])
# 
# 
#     def update(self):
#         self.siirra_hantaa()
#         print(self.hanta)
# 
#         if self.mato.pisteet > len(self.hanta):
#             self.hanta.add(HannanOsa())
#             print('Lisää häntää!')
# 
#     def draw(self, ikkuna):
#         self.hanta.draw(ikkuna)
# 
# class Omena(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
# 
#         self.image = pygame.Surface([5, 5])
#         pygame.draw.rect(self.image, 'red', [0, 0, 5, 5])
#         self.rect = self.image.get_rect()