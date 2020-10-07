import sys
import pygame
from settings import *

pygame.init()
vec = pygame.math.Vector2


class App:
    """Application settings."""
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) #height and width of pygame screen
        self.clock = pygame.time.Clock()
        self.running = True #sets game to automatically run
        self.state = 'start' #initial running state of game
    def run(self):
        """Run Game."""
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            else:
                self.running = False
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

    ########## Helper Functions ################
    def draw_text(self, words, screen, pos, size, color, font_name):
        """Text settings."""
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, color)
        # text_size = text.get_size()
        screen.blit(text, pos)

    ########## Intro Functions ################

    def start_events(self):
        """Game start functionality."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.ley == pygame.K_SPACE:
                self.state = 'playing'

    def start_update(self):
        """Game update functionality."""
        pass
    
    def start_draw(self):
        """Game start screen functionality."""
        self.screen.fill(BLACK) 
        self.draw_text('PUSH SPACE BAR',self.screen, [WIDTH//2, HEIGHT//2], START_TEXT_SIZE, (170, 132, 58), START_FONT)
        pygame.display.upate()
