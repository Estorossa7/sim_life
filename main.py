import pygame
import math
from sys import exit
from random import randint, seed

from config import *
from dna import DNA

class Main:
    def __init__(self, screen):
        self.screen = screen
        self.dna_list = [DNA() for i in range(population)]

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0,0,0))




def game():
    
    screen = pygame.display.set_mode((height , width))

    pygame.display.set_caption('color')

    clock = pygame.time.Clock()

    main_game = Main(screen)

    count = 0

# game loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        main_game.draw()
        main_game.update()

        count += 1
        if count == max_duration:
            run = False
        
        #file =  screen_file + str(count) + '.png'
        #pygame.image.save(screen, file)

        pygame.display.update()
        clock.tick(fps)
    

if __name__=='__main__':
    game()