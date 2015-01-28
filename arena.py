import pygame
import numpy as np

class Arena():
    def __init__(self, canvas, screenSize):
        self.canvas = canvas
        self.screenSize = screenSize
        self.color = (200,200,200)

    def render(self, frame):
        self.canvas.fill((0,0,0))
        pygame.draw.rect(self.canvas, self.color, ((0,0),(self.screenSize[0],self.screenSize[1])), 2)
        if frame  is not None:

            modframe = pygame.surfarray.make_surface(np.rot90(frame))
            modframe = pygame.transform.scale(modframe, tuple(self.screenSize))
            self.canvas.blit(modframe,(0,0))

        for line in range(0,self.screenSize[1]/25):
            pygame.draw.line(self.canvas,  self.color, ((self.screenSize[0]/2),line*25),((self.screenSize[0]/2),line*25+10), (16/4))