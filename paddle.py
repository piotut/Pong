import pygame

class Paddle():
    def __init__(self, canvas, color, screenRect):
        self.canvas = canvas
        self.color = color
        self.screenRect = screenRect
        self.x = 0.0
        self.y = 0.0
        self.height = 150
        self.width = 25
        self.speedMax  = 4.0
        self.speedActual = 0.0
        self.direction = 0;
        self.score = 0

    def setInitialPostition(self, x, y):
        self.x = x
        self.y = y

    def someFancyDebugPrints(self):
        f = pygame.font.Font("gfx/ATARCC__.TTF",20)
        if self.x + 50 > self.screenRect[0]:
            x = self.x - 150
        else:
            x = self.x + 50

        text = f.render('y={}'.format(self.get()['y']), True,(255,0,0))
        self.canvas.blit(text,(x,self.y))
        text = f.render('s={:.2}'.format(self.speedActual), True,(255,0,0))
        self.canvas.blit(text,(x,self.y+20))

    def render(self):
        self.physics()
        pygame.draw.rect(self.canvas, self.color, (self.x,self.y,self.width,self.height))
        #self.someFancyDebugPrints()

    def physics(self):
        if(self.speedActual > 0):
            if(self.direction > 0):
                if(self.y + self.height + self.speedActual < self.screenRect[1]):
                    self.y += self.direction * self.speedActual
                else:
                    self.speedActual = 0.0
            else:
                if(self.y > 0):
                    self.y += self.direction * self.speedActual
            self.speedActual -= 0.1

    def move(self, y):
        self.direction = y
        self.speedActual = self.speedMax

    def get(self):
        return {'x':self.x, 'y':self.y, 'width':self.width, 'height':self.height}

    def incrementScore(self):
        self.score += 1

    def getScore(self):
        return self.score