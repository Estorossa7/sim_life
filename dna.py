from config import *
from util import *
import math


class DNA:
    def __init__(self,idx):
        self.idx = idx
        self.c_r = init_gene_int()
        self.c_g = init_gene_int()
        self.c_b = init_gene_int()

        self.m = ()
        self.f = ()

    def get_color(self):
        return (self.c_r, self.c_g, self.c_b)
    
    def get_position(self):
        return self.idx%20, self.idx//20
           
    def set_parents(self,m,f):
        self.m = m
        self.f = f


def main():
    dna = DNA(1)
    print(dna.get_color())

if __name__=='__main__':
    main()
