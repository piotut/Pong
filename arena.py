import pygame

class Arena():
    def __init__(self, canvas, screenSize):
        self.canvas = canvas
        self.screenSize = screenSize
        self.color = (200,200,200)

    def render(self):
        self.canvas.fill((0,0,0))
        pygame.draw.rect(self.canvas, self.color, ((0,0),(self.screenSize[0],self.screenSize[1])), 2)

        for line in range(0,self.screenSize[1]/25):
            pygame.draw.line(self.canvas,  self.color, ((self.screenSize[0]/2),line*25),((self.screenSize[0]/2),line*25+10), (16/4))