import pyxel
import random

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120

PADDLE_WIDTH = 4
PADDLE_HEIGHT = 20
PADDLE_SPEED = 3


class PongGame:

    def __init__(self):
        pyxel.init(SCREEN_WIDTH,SCREEN_HEIGHT,title="Pyxel Pong")
        
        # Position des raquettes
        self.p1_y = (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2
        self.p2_y = (SCREEN_HEIGHT - PADDLE_HEIGHT) // 2

        # Position de la balle
        self.ball_x = SCREEN_WIDTH // 2
        self.ball_y = SCREEN_HEIGHT // 2

        # Vitesse de la balle
        self.ball_dx = 2
        self.ball_dy = 1.5

        # Scores
        self.score_p1 = 0
        self.score_p2 = 0

        pyxel.run(self.update, self.draw)

    
    def reset_ball(self):
        # Remet la balle au centre
        self.ball_x = SCREEN_WIDTH // 2
        self.ball_y = SCREEN_HEIGHT // 2

        # Redonne sa vitesse
        self.ball_dx = 2
        self.ball_dy = 1.5
    
    def update(self):
        
        # 1. Déplacement J1 (Z / S)
        if pyxel.btn(pyxel.KEY_Z) and self.p1_y > 0:
            self.p1_y -= PADDLE_SPEED
        if pyxel.btn(pyxel.KEY_S) and self.p1_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
            self.p1_y += PADDLE_SPEED
        
        # 2. Déplacement J2 (Haut / Bas)
        if pyxel.btn(pyxel.KEY_UP) and self.p2_y > 0:
            self.p2_y -= PADDLE_SPEED
        if pyxel.btn(pyxel.KEY_DOWN) and self.p2_y < SCREEN_HEIGHT - PADDLE_HEIGHT:
            self.p2_y += PADDLE_SPEED
            
        # Déplacement balle
        self.ball_x += self.ball_dx
        self.ball_y -= self.ball_dy

        # Rebond haut / bas
        if self.ball_y <= 0 or self.ball_y >= SCREEN_HEIGHT - 4:
            self.ball_dy = -self.ball_dy
            
        #Raquette J1
        if self.ball_dx < 0 and self.ball_x <= 5 + PADDLE_WIDTH and self.p1_y <=self.ball_y + 4 and self.ball_y <= self.p1_y + PADDLE_HEIGHT:
            self.ball_dx = -self.ball_dx
            
        #Raquette J2
        if self.ball_dx > 0 and self.ball_x + 4 >= 151 and self.p2_y <= self.ball_y + 4 and self.ball_y <= self.p2_y + PADDLE_HEIGHT:
            self.ball_dx = -self.ball_dx
            
        #Scores
        if self.ball_x < 0:
            self.score_p2 += 1
            self.reset_ball()

        if self.ball_x > SCREEN_WIDTH:
            self.score_p1 += 1
            self.reset_ball()
        
    
    def draw(self):
        pyxel.cls(0)
        
        # Filet
        for y in range(0, SCREEN_HEIGHT, 8):
            pyxel.line(SCREEN_WIDTH // 2, y, SCREEN_WIDTH // 2, y + 4, 13)
        
        #Raquette
        pyxel.rect(5, self.p1_y, PADDLE_WIDTH, PADDLE_HEIGHT, 11)
        pyxel.rect(151, self.p2_y, PADDLE_WIDTH, PADDLE_HEIGHT, 12)
        
        #Balle
        pyxel.rect(self.ball_x,self.ball_y,4,4,7)
        
        # Scores
        pyxel.text(55,10,str(self.score_p1),7)
        pyxel.text(100,10,str(self.score_p2),7)

PongGame()

