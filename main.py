import pygame
import math
from sys import exit
from random import randint, seed

from config import *
from util import *
from dna import DNA

class Main:
    def __init__(self, screen):
        self.screen = screen
        self.dna_list = [DNA(i) for i in range(population)]
        self.fitness_list = {}
        self.child = []


    def update(self):
        for i in range(population):
            key, value = fitness(self.dna_list[i])
            self.fitness_list[key] = value
        
        parents = selection(self.fitness_list.keys())[:200]
        for i in range(int(len(parents)/2)):
            p1, p2 = parents[2*i], parents[2*i+1]
            m, f = self.fitness_list[p1], self.fitness_list[p2] 
            c1, c2 = mate(m,f)
            self.child.append(c1)
            self.child.append(c2)
            

            

    def draw(self):
        self.screen.fill((0,0,0))
        count = 0
        for i in range(20):
            for j in range(20):
                rect = pygame.Rect(j+20*j, i+20*i, 20, 20)
                pygame.draw.rect(self.screen,self.dna_list[count].get_color(),rect)
                count +=1





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
        if count == 1:#max_duration:
            run = False
        
        #file =  screen_file + str(count) + '.png'
        #pygame.image.save(screen, file)

        pygame.display.update()
        clock.tick(fps)
    

if __name__=='__main__':
    game()