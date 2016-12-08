import pygame
from pygame.locals import *

class App:
    def __init__(self):
        self.__running = True
        self.__display__surf = None
        self.size = self.weight, self.height = 900,600

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.__running = True

    def on_event(self,event):
        if (event.type == pygame.QUIT):
            self.__running = False

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if (self.on_init() == False):
            self.__running = False

        while (self.__running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()



if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()