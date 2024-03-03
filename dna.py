from random import randint, randrange
import math


class DNA:
    def __init__(self):
        self.color = self.set_color()

    def set_color(self, random=True):
        if random:
            color = randint(0, 2**24)
        c = "#" + str(hex(color)[2:])
        return c

    def get_parent_gene(self,f,m):
        pass


    def mutation(self, a, b):
        point = randint(0,len(b))

        pass

    def cross_over(self):
        pass

