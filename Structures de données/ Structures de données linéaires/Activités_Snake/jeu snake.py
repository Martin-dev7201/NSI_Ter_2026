import pygame
from snake import Snake
from random import randint

successes, failures = pygame.init()

screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
snake = Snake()
snake.ajout_tete()

FPS = 10  # Frames per second.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
IMAGE = pygame.Surface((10, 10))
IMAGE .fill(WHITE)


def dessiner_serpent(s) :
    '''definir un carre a chaque position du corps de Snake'''
    screen.blit(IMAGE, pygame.Rect((s.valeur[0]*10,s.valeur[1]*10), (s.valeur[0]*10+10, s.valeur[1]*10+10)))
    if s.suivant is not None : dessiner_serpent(s.suivant)

def dessiner_repas(r) :
    '''Definir un carre a la position du repas'''
    screen.blit(IMAGE, pygame.Rect((r[0]*10,r[1]*10), (r[0]*10+10, r[1]*10+10)))

i = 0
play = True
repas = (randint(0,72),randint(0,48))

#########################     boucle de jeu    #########################################################
while play:

    clock.tick(FPS)

    #Changer la position du repas toutes les 10 secondes
    i +=1
    if i == 100 :
        repas = (randint(0,72),randint(0,48))
        i = 0

    # Gestion des touches de controle du serpent
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.lire_orientation() != 'bas' :
                snake.modifier_orientation('haut')
            elif event.key == pygame.K_DOWN and snake.lire_orientation() != 'haut' :
                snake.modifier_orientation('bas')
            elif event.key == pygame.K_LEFT and snake.lire_orientation() != 'droite' :
                snake.modifier_orientation('gauche')
            elif event.key == pygame.K_RIGHT and snake.lire_orientation() != 'gauche' :
                snake.modifier_orientation('droite')
            elif event.key == pygame.K_ESCAPE:
                quit()

    # Deplacer serpent ou agrandir si le repas est mange
    snake.ajout_tete()
    play = not(snake.est_mort())
    if snake.lire_tete() != repas :
        snake.couper_queue()
    else :
        snake.ajout_tete()
        repas = (randint(0,72),randint(0,48))
        i = 0

    # Rafraichissement de l'ecran
    screen.fill(BLACK)
    dessiner_serpent(snake.lire_positions())
    dessiner_repas(repas)
    pygame.display.update()

