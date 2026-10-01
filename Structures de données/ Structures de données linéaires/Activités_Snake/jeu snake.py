import sys
from random import randint
import pygame
from snake import Snake

successes, failures = pygame.init()

screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
snake = Snake()
snake.ajout_tete()

FPS = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
IMAGE = pygame.Surface((10, 10))
IMAGE.fill(WHITE)


def dessiner_serpent(s):
    screen.blit(
        IMAGE,
        pygame.Rect(
            (s.valeur[0] * 10, s.valeur[1] * 10),
            (s.valeur[0] * 10 + 10, s.valeur[1] * 10 + 10),
        ),
    )
    if s.suivant is not None:
        dessiner_serpent(s.suivant)


def dessiner_repas(r):
    screen.blit(
        IMAGE, pygame.Rect((r[0] * 10, r[1] * 10), (r[0] * 10 + 10, r[1] * 10 + 10))
    )


i = 0
play = True
repas = (randint(0, 71), randint(0, 47))
score = 0

print("--- DEBUT DE LA PARTIE ---")
print(f"Score : {score}")

while play:

    clock.tick(FPS)

    i += 1
    if i == 100:
        repas = (randint(0, 71), randint(0, 47))
        i = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.lire_orientation() != "bas":
                snake.modifier_orientation("haut")
            elif event.key == pygame.K_DOWN and snake.lire_orientation() != "haut":
                snake.modifier_orientation("bas")
            elif (
                event.key == pygame.K_LEFT and snake.lire_orientation() != "droite"
            ):
                snake.modifier_orientation("gauche")
            elif (
                event.key == pygame.K_RIGHT and snake.lire_orientation() != "gauche"
            ):
                snake.modifier_orientation("droite")
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Déplacement
    snake.ajout_tete()

    # Gestion de la téléportation aux bords de l'écran (72x48 cases)
    snake.traverser_murs(72, 48)

    # Gestion du repas et du score
    if snake.lire_tete() != repas:
        snake.couper_queue()
    else:
        snake.ajout_tete()
        snake.traverser_murs(72, 48)
        repas = (randint(0, 71), randint(0, 47))
        i = 0
        score += 10
        print(f"Miam ! Score : {score}")

    # Détection de collision avec lui-même
    if snake.est_mort():
        play = False

    # Affichage
    screen.fill(BLACK)
    dessiner_serpent(snake.lire_positions())
    dessiner_repas(repas)
    pygame.display.update()

# Fin de partie
print("\n====================")
print("     GAME OVER      ")
print(f" Score final : {score}")
print("====================")

pygame.quit()
sys.exit()
