# from re import X
import pygame

class Reuna(pygame.sprite.Sprite):
    def __init__(self, leveys : int, korkeus : int):
        super().__init__()
        self.image = pygame.Surface([leveys, korkeus])
        pygame.draw.rect(self.image, 'gray', [0, 0, leveys, korkeus])
        self.rect = self.image.get_rect()

    def siirra(self, x, y):
        self.rect.x = x
        self.rect.y = y

class Mato(pygame.sprite.Sprite):
    def __init__(self, leveys : int, korkeus : int):
        super().__init__()

        self.image = pygame.Surface([leveys, korkeus])

        pygame.draw.rect(self.image, 'blue', [0, 0, leveys, korkeus])

        self.rect = self.image.get_rect()
        self.pisteet = 0

    def siirra_vasemmalle(self, pikselit):
        self.rect.x -= pikselit

    def siirra_oikealle(self, pikselit):
        self.rect.x += pikselit

    def siirra_alas(self, pikselit):
        self.rect.y += pikselit

    def siirra_ylos(self, pikselit):
        self.rect.y -= pikselit

    def syo(self, ruoka : pygame.sprite.GroupSingle):
        tulos = pygame.sprite.spritecollide(self, ruoka, True)
        return tulos

    def lisaa_piste(self):
        self.pisteet += 1
        print(self.pisteet)

    def tormaa(self, reuna : pygame.sprite.Sprite):
        return pygame.sprite.collide_rect(self, reuna)



class Omena(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([5, 5])
        pygame.draw.rect(self.image, 'red', [0, 0, 5, 5])
        self.rect = self.image.get_rect()