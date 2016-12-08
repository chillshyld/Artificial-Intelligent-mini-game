#import the pygame module, and the
#sys module for exiting the window we create
import pygame, sys

#import some useful constants
from pygame.locals import *




#Resources in the map
TREE = 0
DIRT = 1
CAR = 2
STATION = 3
EXIT = 4

#constants representing colours
BLACK = (0,    0,  0  )
BROWN = (153, 76,  0  )
GREEN = (0,  255, 0  )
BLUE  = (0,    0,  255)
WHITE = (255, 255, 255)

#Colors
colours = {
    TREE : GREEN,
    CAR : BLUE,
    DIRT : BROWN,
    STATION : BLACK,
    EXIT : WHITE,
}

#Textures
textures = {
    TREE : pygame.image.load("/Users/Chieh/Desktop/AIProject/Game Resource/trees_1.png"),
    CAR : pygame.image.load("/Users/Chieh/Desktop/AIProject/Game Resource/car_1.jpeg"),
    DIRT : pygame.image.load("/Users/Chieh/Desktop/AIProject/Game Resource/dirt_1.png"),
    STATION : pygame.image.load("/Users/Chieh/Desktop/AIProject/Game Resource/station_1.png"),
    EXIT : pygame.image.load("/Users/Chieh/Desktop/AIProject/Game Resource/exit_1.png"),
}

#Tile MAP
tilemap = [ [TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE],
            [TREE, DIRT, DIRT, DIRT, TREE, DIRT, DIRT, DIRT, TREE, DIRT, DIRT, DIRT, TREE, DIRT, DIRT, DIRT, TREE, EXIT],
            [TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT],
            [TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT],
            [TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT],
            [TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT],
            [TREE, DIRT, DIRT, DIRT, TREE, DIRT, DIRT, DIRT, TREE, DIRT, DIRT, DIRT, TREE, DIRT, DIRT, DIRT, TREE, DIRT],
            [TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT],
            [TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT],
            [TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT],
            [TREE, DIRT, TREE, DIRT, TREE, DIRT, DIRT, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT],
            [TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT],
            [TREE, DIRT, TREE, DIRT, DIRT, DIRT, TREE, DIRT, DIRT, DIRT, TREE, DIRT, DIRT, DIRT, TREE, DIRT, DIRT , DIRT],
            [DIRT, DIRT, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE] ]







#Important dimensions
TILESIZE = 50
MAPWIDTH = 18
MAPHEIGHT = 14




#initialise the pygame module
pygame.init()



#create a new drawing surface, width=300, height=300
DISPLAYSURF = pygame.display.set_mode((TILESIZE * MAPWIDTH,TILESIZE * MAPHEIGHT))
#give the window a caption
pygame.display.set_caption('My First Game')

#the player image
PLAYER = pygame.image.load("/Users/Chieh/Desktop/AIProject/Game Resource/player_1.jpg").convert_alpha()
#the position of the player [x,y]
playerPos = [0,13]


#loop (repeat) forever
while True:

    #get all the user events
    for event in pygame.event.get():
        #if the user wants to quit
        if event.type == QUIT:
            #end the game and close the window
            pygame.quit()
            sys.exit()

        #if any button is pressed
        elif event.type == KEYDOWN:
            # if the right arrow is pressed
            if (event.key == K_RIGHT) and playerPos[0] < MAPWIDTH - 1:
                # change the player's x position
                if (tilemap[playerPos[1]][playerPos[0] + 1] != TREE):
                    playerPos[0] += 1

            # if the left arrow is pressed
            if (event.key == K_LEFT) and playerPos[0] > 0:
                # change the player's x position
                if (tilemap[playerPos[1]][playerPos[0] - 1] != TREE):
                    playerPos[0] -= 1

            # if the up arrow is pressed
            if (event.key == K_UP) and playerPos[1] > 0:
                # change the player's y position
                if (tilemap[playerPos[1] - 1][playerPos[0]] != TREE):
                    playerPos[1] -= 1
            # if the down arrow is pressed
            if (event.key == K_DOWN) and playerPos[1] < MAPHEIGHT - 1:
                # change the player's y position
                if (tilemap[playerPos[1] + 1][playerPos[0]] != TREE):
                    playerPos[1] += 1


    # loop through each row
    for row in range(MAPHEIGHT):
        # loop through each column in the row
        for column in range(MAPWIDTH):
            # draw the resource at that position in the tilemap, using the correct colour
            # pygame.draw.rect(DISPLAYSURF, colours[tilemap[row][column]],
            #                  (column * TILESIZE, row * TILESIZE, TILESIZE, TILESIZE))

            # draw an image for the resource, in the correct position
            DISPLAYSURF.blit(textures[tilemap[row][column]], (column * TILESIZE, row * TILESIZE))
            # display the player at the correct position
            DISPLAYSURF.blit(PLAYER, (playerPos[0] * TILESIZE, playerPos[1] * TILESIZE))

    #update the display
    pygame.display.update()

