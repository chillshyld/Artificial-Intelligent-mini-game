import os, sys
import pygame
from pygame.locals import *
from Game.BlockSprites import Dirt,Exit,Station,Tree, Car, Map
from Game.Constant import *

class App:
    """The Main App Class - This class handles the main
    initialization and creating of the Game."""

    def __init__(self, width=MAPWIDTH * TILESIZE,height=MAPHEIGHT * TILESIZE):
        """Initialize PyGame"""
        pygame.init()
        """Set the window Size"""
        self.width = width
        self.height = height
        """Create the Screen"""
        self.screen = pygame.display.set_mode((self.width
                                               , self.height))
        """Create Map """
        self.map = Map(MAPHEIGHT, MAPWIDTH, TILESIZE, tilemap)

    def LoadSprites(self):
        """Load the sprites that we need"""

        init_row = MAPHEIGHT - 1
        init_col = 0
        self.car = Car((init_col * TILESIZE,init_row * TILESIZE ))
        self.car_sprites = pygame.sprite.RenderPlain(self.car)

        """Create object sprites"""
        self.tree_sprites = pygame.sprite.Group()
        self.station_sprites = pygame.sprite.Group()
        self.exit_sprites = pygame.sprite.Group()
        self.dirt_sprites = pygame.sprite.Group()

        """Fill Screen with sprites"""
        for row in range(self.map.GetHeight()):
            for col in range(self.map.GetWidth()):
                if (self.map.tileMap[row][col] == TREE):
                    self.tree_sprites.add(Tree(pygame.Rect(col * self.map.tileSize ,row * self.map.tileSize,50,50)))
                elif (self.map.tileMap[row][col] == CAR):
                    self.dirt_sprites.add(Dirt(pygame.Rect(col * self.map.tileSize, row * self.map.tileSize, 50, 50)))
                    continue
                elif (self.map.tileMap[row][col] == STATION):
                    self.station_sprites.add(Station(pygame.Rect(col * self.map.tileSize, row * self.map.tileSize, 50, 50)))
                elif (self.map.tileMap[row][col] == EXIT):
                    self.exit_sprites.add(Exit(pygame.Rect(col * self.map.tileSize, row * self.map.tileSize, 50, 50)))
                elif (self.map.tileMap[row][col] == DIRT):
                    self.dirt_sprites.add(Dirt(pygame.Rect(col * self.map.tileSize, row * self.map.tileSize, 50, 50)))
                elif (self.map.tileMap[row][col] == EMPTY):
                    continue



    def MainLoop(self):
        """This is the Main Loop of the Game"""
        """Load All of our Sprites"""
        self.LoadSprites()
        """tell pygame to keep sending up keystrokes when they are
        held down"""
        pygame.key.set_repeat(500, 30)

        """Create the background"""
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))

        while True:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    sys.exit(1)
                elif (event.type == KEYDOWN):
                    if ((event.key == K_RIGHT) or (event.key == K_LEFT) or (event.key == K_UP) or (event.key == K_DOWN)):
                        self.map.moveCar(event.key,self.car)

            self.screen.blit(self.background, (0, 0))
            self.DrawText()
            """Draw sprites"""
            self.DrawSprites()
            pygame.display.flip()

    def DrawText(self):
        """Do the Drawging"""

        if pygame.font:
            font = pygame.font.Font(None, 36)
            text = font.render("Fuel Remaining:  %s" % self.car.fuels
                               , 1, (255, 0, 0))
            textpos = text.get_rect(centerx=self.background.get_width() / 5, centery = 30)
            text2 = font.render("Budget Used:  %s $" % self.car.budget
                               , 1, (255, 0, 0))
            textpos2 = text.get_rect(centerx=self.background.get_width() * 4 / 5, centery=30)
            self.screen.blit(text, textpos)
            self.screen.blit(text2, textpos2)

    def DrawSprites(self):
        self.car_sprites = pygame.sprite.RenderPlain(self.car)
        self.dirt_sprites.draw(self.screen)
        self.tree_sprites.draw(self.screen)
        self.station_sprites.draw(self.screen)
        self.exit_sprites.draw(self.screen)
        self.car_sprites.draw(self.screen)




if __name__ == "__main__":
    MainWindow = App()
    MainWindow.MainLoop()


