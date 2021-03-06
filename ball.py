import pygame
from random import randint

WIDTH = 0
HEIGHT = 1

class Ball():
	def __init__(self, canvas, color, screenSize, soundHandler):
		self.canvas = canvas
		self.color = color
		self.screenSize = screenSize
		self.soundHandler = soundHandler
		self.x = 0
		self.y = 0
		self.speedX = 10
		self.speedY = 10
		self.radius = 15

	def setInitialPostition(self, x, y):
		self.x = x
		self.y = y

	def render(self):
		self.physics()
		pygame.draw.circle(self.canvas, self.color, (int(self.x),int(self.y)), self.radius)

	def physics(self):
		if(self.y + self.radius > self.screenSize[HEIGHT]) or (self.y - self.radius < 0):
			self.speedY = -self.speedY
			self.soundHandler.wall()

		self.x += self.speedX
		self.y += self.speedY


	def bounce(self):
		self.speedX *= -1 

	def reset(self):
		self.x  = self.screenSize[WIDTH] / 2;
		self.y  = self.screenSize[HEIGHT] / 2;

	def resetToLeft(self):
		self.reset()
		if(self.speedX > 0):
			self.speedX *= -1 

	def resetToRight(self):
		self.reset()
		if(self.speedX < 0):
			self.speedX *= -1 

	def get(self):
		return {'x':self.x, 'y':self.y, 'radius': self.radius}