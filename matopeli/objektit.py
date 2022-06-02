import pygame

pygame.init()

class Mato(pygame.sprite.Sprite):
    def __init__(self, nopeus : int):
        super().__init__()

    def liiku_alas(self):
        pass

    def liiku_ylos(self):
        pass

    def liiku_vasemmalle(self):
        pass

    def liiku_oikealle(self):
        pass

if __name__ == '__main__':
    leveys = 800
    korkeus = 600

    kaynnissa = True

    ikkuna = pygame.display.set_mode((leveys, korkeus))
    pygame.display.set_caption('MATOPELI')

    while kaynnissa:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                kaynnissa = False

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