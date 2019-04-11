import pygame
from pygame.locals import *

pygame.init() # on doit initialiser pygame avant d'appler les fonction.

fenetre = pygame.display.set_mode((800, 600)) #  largeur = 800 et longueur= 600

clock = pygame.time.Clock()

# creation de notre joueur(acteur) sous forme de class
class Acteur(pygame.sprite.Sprite):
    def __init__(self):
        super(Acteur, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 100, 23))
        self.rect = self.surf.get_rect()

    def update(self, bouton_appyer):
        if bouton_appyer[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if bouton_appyer[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if bouton_appyer[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if bouton_appyer[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)

        # maintenir acteur dans la fenetre

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 600:
            self.rect.bottom = 600


# Creer une instance de Action que je vais appele Sidi
sidi = Acteur()

# la variable pour savoir etat d'execution du jeu.
execution = True

while execution:
    # parcourir tout evenement de pygame avec la boucle for
    for event in pygame.event.get():
        # on verifie si on appuye sur un bouton
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                execution = False

        elif event.type == pygame.QUIT:
            execution = False

    bouton_appyer = pygame.key.get_pressed() # determine quelle bouton a ete appuyer.
    sidi.update(bouton_appyer) # on appele la foncton update pour faire deplace acteur par consequent

    fenetre.fill((0, 0, 0))

    # desiner le acteur sur l'ecran a la position 400 x 300
    fenetre.blit(sidi.surf, sidi.rect)
    # mettre a jours l'ecran
    pygame.display.flip()
    clock.tick(60)

