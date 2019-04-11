import pygame
from pygame.locals import *

pygame.init() # on doit initialiser pygame avant d'appler les fonction.

fenetre = pygame.display.set_mode((800, 600)) #  largeur = 800 et longueur= 600


# creation de notre joueur(acteur) sous forme de surface dont la taille 50x50
surf = pygame.Surface((50, 50))
# definir la couleur de de notre acteur
surf.fill((255, 255 , 255))
rect = surf.get_rect()

# la variable pour savoir etat d'execution du jeu.
execution = True

while execution:
    # parcourir tout evenement de pygame avec la boucle for
    for event in pygame.event.get():
        # on verifie si on appuye sur un boutton
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                execution = False

        elif event.type == pygame.QUIT:
            execution = False


    # desiner le acteur sur l'ecran a la position 400 x 300
    fenetre.blit(surf, (400, 300))
    # mettre a jours l'ecran
    pygame.display.flip()

