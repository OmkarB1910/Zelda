import pygame
import sys
from settings import *
from level import Level
 
 
class Game:
    def __init__(self):
        pygame.init() #initiating pygame
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) #display surface
        pygame.display.set_caption('Zelda Game') #set the title of the game
        self.clock = pygame.time.Clock()    #set clock
        
        self.level = Level()    #instance of the level
        # self.running = True

    def run(self):
        while True: #game loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #check for closing the game window
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black') #fill the screen with black color
            self.level.run()
            pygame.display.update() #update the display
            self.clock.tick(FPS)   #set the fps


if __name__ == '__main__':
    game = Game() #instace of the game
    game.run()  #run the game using run() method
