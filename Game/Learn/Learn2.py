import os, sys
import pygame
from pygame.locals import *

if not pygame.font: print ('Warning, fonts disabled')
if not pygame.mixer: print ('Warning, sound disabled')

class PyManMain:
    """The Main PyMan Class - This class handles the main
    initialization and creating of the Game."""

    def __init__(self, width=900,height=600):
        """Initialize"""
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width
                                               , self.height))

    def MainLoop(self):
        """This is the Main Loop of the Game"""
        self.LoadSprites()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if (event.type == KEYDOWN):
                    if ((event.key == K_RIGHT)
                        or (event.key == K_LEFT)
                        or (event.key == K_UP)
                        or (event.key == K_DOWN)):
                        self.player.move(event.key)

            """Check for collision"""
            lstCols = pygame.sprite.spritecollide(self.player
                                                  , self.pellet_sprites
                                                  , True)
            """Update the amount of pellets eaten"""
            self.player.pellets = self.player.pellets + len(lstCols)
            self.player_sprites.draw(self.screen)
            self.pellet_sprites.draw(self.screen)

            pygame.display.flip()

    def LoadSprites(self):
        """Load the sprites that we need"""
        self.player = Player()
        self.player_sprites = pygame.sprite.RenderPlain((self.player))

        """figure out how many pellets we can display"""
        nNumHorizontal = int(self.width / 50)
        nNumVertical = int(self.height / 50)
        """Create the Pellet group"""
        self.pellet_sprites = pygame.sprite.Group()
        """Create all of the pellets and add them to the
        pellet_sprites group"""
        for x in range(nNumHorizontal):
            for y in range(nNumVertical):
                self.pellet_sprites.add(Pellet(pygame.Rect(x * 50, y * 50, 50, 50)))


class Player(pygame.sprite.Sprite):
    """This is our player that will move around the screen"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("/Users/Chieh/Desktop/AIProject/Game Resource/player_1.jpg")
        self.rect = self.image.get_rect()
        self.pellets = 0
        self.x_dist = 50
        self.y_dist = 50

    def move(self, key):
        """Move your self in one of the 4 directions according to key"""
        """Key is the pyGame define for either up,down,left, or right key
        we will adjust ourselves in that direction"""
        xMove = 0;
        yMove = 0;

        if (key == K_RIGHT):
            xMove = self.x_dist
        elif (key == K_LEFT):
            xMove = -self.x_dist
        elif (key == K_UP):
            yMove = -self.y_dist
        elif (key == K_DOWN):
            yMove = self.y_dist
        self.rect.move_ip(xMove, yMove);


class Pellet(pygame.sprite.Sprite):


    def __init__(self, rect=None):
        pygame.sprite.Sprite.__init__(self)
        self.image =  pygame.image.load("/Users/Chieh/Desktop/AIProject/Game Resource/trees_1.png")
        self.rect = self.image.get_rect
        if rect != None:
            self.rect = rect



if __name__ == "__main__":
    MainWindow = PyManMain()
    MainWindow.MainLoop()