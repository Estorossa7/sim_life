import pygame
import math
from sys import exit
from random import randint, seed

from config import *
from dna import DNA

class Ball:
    def __init__(self,idx) -> None:
        self.ball_idx = idx
        #self.dna = DNA()
        self.v_x = 0 #randint(-3,3)
        self.v_y = 0 #randint(-3,3)
        self.x , self.y = self.get_init_position(self.ball_idx)

        self.influence = 50
        self.repel = 0.1

    def get_init_position(self,idx,flag=False):
        if flag:
            x, y = randint(0,height), randint(0,width)
        else:
            dst = math.pow(idx / (num_ball - 1),pow)
            angle = 2 * math.pi * turn_fraction * idx

            x = dst * math.cos(angle) * scale
            y = dst * math.sin(angle) * scale
            print(x,y)
        return x+offset, y+offset


    def get_influence(self, ball_list):
        x, y = 0, 0
        count = 0
        for i in ball_list:
            if i.x > (self.x - self.influence) and i.x < (self.x + self.influence) and i.y > (self.y - self.influence) and i.y < (self.y + self.influence): 
                count +=1
                x = x + (self.x - i.x) * self.repel
                y = y + (self.y - i.y) * self.repel

        return x/count, y/count

    def update(self, ball_list):
        influ_x, influ_y = 0,0 #self.get_influence(ball_list)
        self.x = self.x + self.v_x + influ_x
        self.y = self.y + self.v_y + influ_y

        #self.dna.set_color()

    def draw_ball(self,screen):
        particle_rect = pygame.Rect(self.x, self.y, ball_height,ball_width)
        pygame.draw.rect( screen, ball_color, particle_rect)

    def check_border_collisions(self):
        if self.x < 0:
            self.v_x = self.v_x * (-1)
            self.x = 0
        elif self.y < 0:
            self.v_y = self.v_y * (-1)
            self.y = 0
        elif self.x > height:
            self.v_x = self.v_x * (-1)
            self.x = height
        elif self.y > width:
            self.v_y = self.v_y * (-1)
            self.y = width

class Main:
    def __init__(self, screen):
        self.screen = screen
        self.ball_list = [Ball(i) for i in range(num_ball)]

    def update(self):
        for i in self.ball_list:
            i.update(self.ball_list)
            i.check_border_collisions()

    def draw(self):
        self.screen.fill((0, 0, 0))
        for i in self.ball_list:
            i.draw_ball(self.screen)



def game():
    
    screen = pygame.display.set_mode((height , width ))

    pygame.display.set_caption('graphs')

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

        main_game.update()

        main_game.draw()
        
        count += 1
        if count == max_duration:
            run = False
        
        file =  screen_file + str(count) + '.png'
        #pygame.image.save(screen, file)

        pygame.display.update()
        clock.tick(fps)
    

if __name__=='__main__':
    game()