#!/usr/bin/python
import pygame
from pygame.locals import *  # importujemy nazwy (klawiszy)
from sys import exit
from math import *
from random import randint

#internal classes
from paddle import Paddle
from ball import Ball
from arena import Arena
from referee import Referee

screenWidth = 800
screenHeight = 600      # ustalamy rozmiar ekranu
screenRect = (screenWidth,screenHeight)

class Pong(object):
    def __init__(self):
        pygame.init()       # incjalizujemy biblioteke pygame
        self.fps = pygame.time.Clock()
        flag = DOUBLEBUF    # wlaczamy tryb podwojnego buforowania

        # tworzymy bufor na  grafike
        self.board = pygame.display.set_mode(screenRect, flag)
        pygame.display.set_caption(' --- Pong --- ')

        # zmienna stanu gry
        self.state = 1  # 1 - run, 0 - exit

        self.p1 = Paddle(self.board, (200,100,100),screenRect)
        self.p1.setInitialPostition(0,screenHeight/2)

        self.p2 = Paddle(self.board, (100,200,100),screenRect)
        self.p2.setInitialPostition(screenWidth-25,screenHeight/2)

        self.ball = Ball(self.board, (50,50,250), screenRect)
        self.ball.setInitialPostition(320,240)

        self.arena = Arena(self.board, screenRect)

        self.referee = Referee(self.ball, self.p1, self.p2, screenRect)

        self.loop()           # glowna petla gry

    def movep1(self, diry):
       '''obsluga ruchow dla player1'''
       self.p1.move(diry)

    def movep2(self, diry):
       '''obsluga ruchow dla player2'''
       self.p2.move(diry)

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
              self.movep1(1)  # ruch w dol - p1

            if keys[K_a]:
              self.movep1(-1)   # ruch w gore - p1
            if keys[K_m]:
              self.movep2(1)  # ruch w dol - p2

            if keys[K_k]:
              self.movep2(-1)   # ruch w gore - p2

            self.arena.render()

            font = pygame.font.Font("gfx/ATARCC__.TTF",40)
            text1 = font.render('P1={}'.format(self.p1.getScore()), True,(200,200,200))
            text2 = font.render('P2={}'.format(self.p2.getScore()), True,(200,200,200))
                   
            quartWidth = screenWidth/4
            self.board.blit(text1,(quartWidth * 1 - quartWidth/2,10))
            self.board.blit(text2,(quartWidth * 3 - quartWidth/2,10))

            self.p1.render()
            self.p2.render()
            self.ball.render()
            self.referee.judge()

            pygame.display.flip()   # wyswietlamy obrazki
            self.fps.tick(150)

        self.game_exit()

if __name__ == '__main__':
   Pong()
