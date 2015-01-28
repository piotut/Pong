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
from sound import Sound
from referee import Referee
from tracking import Tracking

from threading import Thread

screenWidth = 1200
screenHeight = 600
screenRect = (screenWidth,screenHeight)

class Pong(object):
    def __init__(self, file1=None, file2=None):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        self.fps = pygame.time.Clock()
        flag = DOUBLEBUF

        self.board = pygame.display.set_mode(screenRect, flag)
        pygame.display.set_caption('[ --- Pong --- ]')

        self.state = 1  # 1 - run, 0 - exit

        self.track = Tracking(file1, file2)

        self.sound = Sound()
        self.p1 = Paddle(self.board, (200,100,100),screenRect)
        self.p1.setInitialPostition(0,screenHeight/2)
        self.p2 = Paddle(self.board, (100,200,100),screenRect)
        self.p2.setInitialPostition(screenWidth-self.p2.get()['width'],screenHeight/2)
        self.ball = Ball(self.board, (50,50,250), screenRect, self.sound)
        self.ball.setInitialPostition(screenWidth/2,screenHeight/2)
        self.arena = Arena(self.board, screenRect)
        self.referee = Referee(self.ball, self.p1, self.p2, screenRect, self.sound)

        

        self.t = Thread(target=self.track.run)
        #self.track.run()
        self.t.start()

        self.p1_pos = 0
        self.p2_pos = 0

        self.loop()

    def movep1(self, diry):
       '''Player1 moves support'''
       self.p1.move(diry)

    def movep2(self, diry):
       '''Player2 moves support'''
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


            dirp1 = copysign(1, self.track.p1_position - self.p1_pos)
            dirp2 = copysign(1, self.track.p2_position - self.p2_pos)

            self.p1_pos += dirp1
            self.p2_pos += dirp2

            self.p1.set(self.track.p1_position+45)
            self.p2.set(self.track.p2_position+45)
            
            if keys[K_f]:
                pygame.display.toggle_fullscreen()

            self.arena.render(self.track.frame)

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
            self.fps.tick(80)

        self.track.running = False 
        self.game_exit()
        

if __name__ == '__main__':
   Pong('czerwony.txt', 'zielony.txt')
