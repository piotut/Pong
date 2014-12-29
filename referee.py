WIDTH = 0
HEIGHT = 1

class Referee():
    def __init__(self, ball, playerLeft, playerRight, screenSize, soundHandle):
        self.ball = ball
        self.playerLeft = playerLeft
        self.playerRight = playerRight
        self.screenSize = screenSize
        self.sound = soundHandle

    def collision(self, ball, player):
    	ballParams = ball.get()
    	ballX = ballParams['x']
    	ballY = ballParams['y']
    	ballR = ballParams['radius']

    	playerParams = player.get()
    	playerX = playerParams['x']
    	playerY = playerParams['y']
    	playerW = playerParams['width']
    	playerH = playerParams['height']

    	return (ballX - ballR < playerX + playerW) and \
    		(ballX + ballR > playerX) and \
    		(ballY < playerY + playerH) and \
    		(ballR + ballY > playerY)    		

    def judge(self):
    	ballParams = self.ball.get()
    	ballX = ballParams['x'];
    	ballY = ballParams['y'];
    	ballRadius = ballParams['radius'];

    	if ballX + ballRadius > self.screenSize[WIDTH]:
    		self.ball.resetToLeft()
    		self.playerLeft.incrementScore()
    		self.sound.win()

    	if ballX - ballRadius < 0:
    		self.ball.resetToRight()
    		self.playerRight.incrementScore()
    		self.sound.win()

    	if self.collision(self.ball, self.playerLeft):
    		self.ball.bounce()
    		self.sound.bounce()

    	if self.collision(self.ball, self.playerRight):
    		self.ball.bounce()
    		self.sound.bounce()
