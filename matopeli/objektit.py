import pygame
import random

pygame.init()

class Mato(pygame.sprite.Sprite):
    def __init__(self, nopeus : int):
        super().__init__()
        self.nopeus = nopeus
        self.pisteet = 0

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

    def lisaa_piste(self):
        self.pisteet += self.nopeus

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
        # pygame.draw.circle(self.image, self.color, (self.x, self.y), self._sivu / 2)
        pygame.draw.rect(self.image, 'gray', [0, 0, 10, 10])
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y

class Ruoka(pygame.sprite.Sprite):
    def __init__(self, ikkuna):
        super().__init__()
        self.ruoka = pygame.sprite.GroupSingle()

        self.image = pygame.Surface([5, 5])
        pygame.draw.rect(self.image, 'red', [0, 0, 5, 5])
        self.rect = self.image.get_rect()

        self.sijoita_ruoka(ikkuna)
        self.ruoka.add(self)

    def sijoita_ruoka(self, ikkuna):
        lev, kork = ikkuna.get_size()
        self.rect.x = random.randint(0, lev-5)
        self.rect.y = random.randint(0, kork-5)

    def on_syoty(self, mato):
        for paa in mato.paa:
            tulos = pygame.sprite.spritecollide(paa, self.ruoka, True)
        return tulos

    def piirra(self, ikkuna):
        self.ruoka.draw(ikkuna)

class Kontrollit:
    def __init__(self):
        self.alusta_kontrollit()

    def alusta_kontrollit(self):
        self.kontrollit = {
            'ylös' : False,
            'alas' : False,
            'vasemmalle' : False,
            'oikealle' : False
        }

    def tarkista_nappain(self, tapahtuma):
        '''
        Tarkistaa, mitä nuolinäppäintä on painettu.
        Muita näppäimiä ei tueta.

        Palauttaa kontrollit sanakirjana. Sanakirja on
        muotoa

        kontrollit = {
            'ylös' : Bool,
            'alas' : Bool,
            'vasemmalle' : Bool,
            'oikealle' : Bool
        }
        '''
        try:
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_UP:
                    if not self.kontrollit['alas']:
                        self.alusta_kontrollit()
                        self.kontrollit['ylös'] = True
                elif tapahtuma.key == pygame.K_DOWN:
                    if not self.kontrollit['ylös']:
                        self.alusta_kontrollit()
                        self.kontrollit['alas'] = True
                elif tapahtuma.key == pygame.K_LEFT:
                    if not self.kontrollit['oikealle']:
                        self.alusta_kontrollit()
                        self.kontrollit['vasemmalle'] = True
                elif tapahtuma.key == pygame.K_RIGHT:
                    if not self.kontrollit['vasemmalle']:
                        self.alusta_kontrollit()
                        self.kontrollit['oikealle'] = True
            return self.kontrollit
        except AttributeError:
            print('Virheellinen argumentti')
            return None


if __name__ == '__main__':
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