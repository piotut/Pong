import pygame
from pygame.locals import *  # importujemy nazwy (klaiwszy)
from sys import exit
from math import *
from random import randint

screen_size = (800,600)      # ustalamy rozmiar ekranu

class Pong(object):
    def __init__(self):
        pygame.init()       # incjalizujemy biblioteke pygame
        flag = DOUBLEBUF    # wlaczamy tryb podwojnego buforowania

        # tworzymy bufor na  grafike
        self.board = pygame.display.set_mode(screen_size, flag)

        # zmienna stanu gry
        self.state = 1  # 1 - run, 0 - exit
        self.image = [None] *3
        self.image[2] = pygame.image.load('circle.png')
        self.image[1] = pygame.image.load('rectangle.png')
        self.image[0] = pygame.image.load('rectangle2.png')
        self.player2_x = 0   # pozycja x dla p2
        self.player2_y = 0    # pozycja y dla p2
        self.speed = 1
        self.player1_x = 784   # pozycja x dla p1
        self.player1_y = 0   # pozycja y dla p1
        self.circle_x = 350
        self.circle_y = 350

        self.p = [0,0]

        self.direct = [-1, -1]

        self.loop()           # glowna petla gry

    def movep1(self,dirx, diry):
       '''obsluga ruchow dla player1'''
       self.player1_x += (dirx * self.speed)
       self.player1_y += (diry * self.speed)

    def movep2(self,dirx, diry):
       '''obsluga ruchow dla player2'''
       self.player2_x += (dirx * self.speed)
       self.player2_y += (diry * self.speed)

    def move_circle(self):
        '''obsluga ruchow dla circle'''
        self.circle_x += self.direct[0]*self.speed
        self.circle_y += self.direct[1]*self.speed
        if self.circle_x == 0:
            self.p[1] += 1
            self.circle_x = 350
        elif self.circle_x + 40 == 800:
            self.p[0] += 1
            self.circle_x = 350
        if self.circle_y in (0, 560):
            self.direct[1] = -1 * self.direct[1]

        if self.collision(self.circle_y, 40, 40, self.player2_y, 16, 200) and self.direct[0] == -1 and self.circle_x == self.player2_x + 16:
            self.direct[0] = -1 * self.direct[0]

        if self.collision(self.circle_y, 40, 40, self.player1_y, 16, 200) and self.direct[0] == 1 and self.circle_x + 40 == self.player1_x:
            self.direct[0] = -1 * self.direct[0]

    def collision(self, cy, c_width, c_height, py, p_width, p_height):
        '''wykrycie zderzenia z belkami'''
        return(cy<py+p_height and cy>py) or (cy+c_width>py and cy+c_width<py+p_height)  

    def game_exit(self):
        exit()

    def loop(self):
        flaga = 1
        while self.state==1:
           for event in pygame.event.get():
               if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                   self.state=0

           keys = pygame.key.get_pressed()

           if keys[K_z]:
              self.movep1(0,1)  # ruch w dol - p1

           if keys[K_a]:
              self.movep1(0,-1)   # ruch w gore - p1

           if keys[K_m]:
              self.movep2(0,1)  # ruch w dol - p2

           if keys[K_k]:
              self.movep2(0,-1)   # ruch w gore - p2

           self.move_circle()

           self.board.fill((255,255,255))  # czyscimy ekran
           font = pygame.font.SysFont("calibri",40)
           text = font.render('{} - {}'.format(self.p[0], self.p[1]), True,(0,0,0))
                   
           self.board.blit(text,(340,10))
           self.board.blit(self.image[2],(self.circle_x,self.circle_y))
           self.board.blit(self.image[1],(self.player1_x,self.player1_y))
           self.board.blit(self.image[0], (self.player2_x,self.player2_y))
           pygame.display.flip()   # wyswietlamy obrazki

        self.game_exit()

if __name__ == '__main__':
   Pong()
