import sys
import pygame 
from settings import *

pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'Intro'
        
    def run(self):
        while self.running:
            pygame.event.get()
            if self.state == 'intro':
                self.intro_events()
                self.intro_update()
                self.intro_draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
    
    ########## Intro Functions ################

    def intro_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def intro_update(self):
        pass

    def intro_draw(self):
        pygame.display.upate()