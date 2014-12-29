import pygame

class Sound():
	def __init__(self):
		self.beep = pygame.mixer.Sound('snd/beep.ogg')
		self.peep = pygame.mixer.Sound('snd/peep.ogg')
		self.plop = pygame.mixer.Sound('snd/plop.ogg')

	def bounce(self):
		self.beep.play()

	def wall(self):
		self.plop.play()

	def win(self):
		self.peep.play()