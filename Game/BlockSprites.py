import pygame
from pygame.locals import *
from Game.Constant import *

class Tree(pygame.sprite.Sprite):
    def __init__(self,rect = None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("/Users/Chieh/Desktop/AIProject/Game Resource/Images/tree_bg_1.png")
        self.rect = self.image.get_rect()
        if rect != None:
            self.rect = rect

class Station(pygame.sprite.Sprite):
    def __init__(self,rect = None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("/Users/Chieh/Desktop/AIProject/Game Resource/Images/station_2.png")
        self.rect = self.image.get_rect()
        if rect != None:
            self.rect = rect

class Exit(pygame.sprite.Sprite):
    def __init__(self, rect = None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("/Users/Chieh/Desktop/AIProject/Game Resource/Images/exit_2.png")
        self.rect = self.image.get_rect()
        if rect != None:
            self.rect = rect

class Dirt(pygame.sprite.Sprite):
    def __init__(self,rect = None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("/Users/Chieh/Desktop/AIProject/Game Resource/Images/dirt_1.png")
        self.rect = self.image.get_rect()

        if rect != None:
            self.rect = rect

class Car(pygame.sprite.Sprite):
    def __init__(self,initial_pos = (0,0)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("/Users/Chieh/Desktop/AIProject/Game Resource/Images/player_1.jpg")
        """Set car initial position"""
        self.cur_row = initial_pos[1]//TILESIZE
        self.cur_col = initial_pos[0]//TILESIZE
        self.rect = self.image.get_rect().move(initial_pos)
        self.fuels = 10
        self. budget = 0
        """Set the number of Pixels to move each time"""
        self.x_dist = 50
        self.y_dist = 50

        self.MAX_FUEL = 10



    def move(self,key):
        """Move your self in one of the 4 directions according to key"""
        """Key is the pyGame define for either up,down,left, or right key
        we will adjust outselfs in that direction"""
        xMove = 0
        yMove = 0

        if (key == K_RIGHT):
            xMove = self.x_dist
            self.cur_col += 1
        elif (key == K_LEFT):
            xMove = -self.x_dist
            self.cur_col -= 1
        elif (key == K_UP):
            yMove = -self.y_dist
            self.cur_row -= 1
        elif (key == K_DOWN):
            yMove = self.y_dist
            self.cur_row += 1
        # self.rect = self.rect.move(xMove,yMove);
        self.fuels -= 1
        self.rect.move_ip(xMove, yMove)

    def getCurrentPosition(self):
        return [self.cur_row,self.cur_col]

class Map:
    def __init__(self,width = 0, height = 0,tileSize = 10,map = None):
        self.initMapProperties(width,height,tileSize,map)
        """Find initial point of car"""
        self.findCar()


    def initMapProperties(self,width,height,tileSize,map):
        self.tileMap = map
        self.mapHeight = width
        self.mapWidth = height
        self.tileSize = tileSize
        self.car_cur_col = ''
        self.car_cur_row = ''



    def findCar(self):
        for row in range(self.mapHeight):
            for col in range(self.mapWidth):
                if (self.tileMap[row][col] == CAR):
                    self.car_cur_col = col
                    self.car_cur_row = row
                    break
        if (self.car_cur_col == '' and self.car_cur_row == ''):
            print("No car on the map")


    def moveCar(self,key,car):
        car_pos = car.getCurrentPosition()
        row = car_pos[0]
        col = car_pos[1]
        """Check whether car can move to its desirable direction"""
        can_move = True
        if (key == K_RIGHT):
            if (self.tileMap[row][col + 1] == TREE or self.tileMap[row][col + 1] == EMPTY ):
                return False
        elif (key == K_LEFT):
            if (self.tileMap[row][col - 1] == TREE or self.tileMap[row][col - 1] == EMPTY):
                return False
        elif (key == K_UP):
            if (self.tileMap[row - 1][col] == TREE or self.tileMap[row - 1][col] == EMPTY):
                return False
        elif (key == K_DOWN):
            if (self.tileMap[row + 1][col] == TREE or self.tileMap[row + 1][col] == EMPTY):
                return False
        """move the car and check its location whether is on block other than type tree"""
        if (can_move):
            car.move(key)
            car_pos = car.getCurrentPosition()
            row = car_pos[0]
            col = car_pos[1]
            if (self.tileMap[row][col]==STATION):

                fuel_cost = (car.MAX_FUEL - car.fuels)* 0.7
                car.budget += fuel_cost
                car.fuels = car.MAX_FUEL
            elif (self.tileMap[row][col]==EXIT):
                print("Goal has been reached!!!")

    # def UpdateCarPos(self,pos):
    #     self.car_cur_row = pos[0]
    #     self.car_cur_col = pos[1]
    #     if (self.tileMap[row][col] == STATION):
    #         car.fuel = car.MAX_FUEL
    #     elif (self.tileMap[row][col] == EXIT):
    #         print("Goal has been reached!!!")


    def LoadMap(self):
        pass


    def GetWidth(self):
        return self.mapWidth

    def GetHeight(self):
        return self.mapHeight