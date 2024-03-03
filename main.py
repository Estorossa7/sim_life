import pygame
import math
import time
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
            value, key = fitness(self.dna_list[i])            #flipped
            self.fitness_list[key] = value
        parents = dict(sorted(self.fitness_list.items(), key=lambda item: item[1]))
        sort_genes = list(parents.keys())[:200]

        print(len(sort_genes))
        
        for i in range(int(len(sort_genes)/2)):
            m, f = sort_genes[2*i], sort_genes[2*i+1]
            c = mate(m,f)
            for j in c:
                self.child.append(j)

        for i in range(population):
            self.dna_list[i].reset_gene(self.child[i])
        
        print(len(self.child))
        self.fitness_list = dict()
        self.child = list()

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

        start = time.time()
        main_game.draw()
        main_game.update()
        stop = time.time()

        count += 1
        if count == max_duration:
            run = False
        
        #file =  screen_file + str(count) + '.png'
        #pygame.image.save(screen, file)

        print(f"frame: {count}, time: {stop - start}")              ##########

        pygame.display.update()
        clock.tick(fps)
    

if __name__=='__main__':
    game()