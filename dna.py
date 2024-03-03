from config import *
from random import randint, random
import math

#   initialises genes
def init_gene_str(a = 8):
    r = pow(2,a)
    num = randint(0,r-1)
    gene = bin(num)[2:].zfill(8)
    return gene

def init_gene_int(a=8):
    return randint(0,pow(2,a)-1)

#   get gene from int to string
def convert_int_str(x, base = 2):
    return bin(x)[2:].zfill(8)

#   get gene from str to int
def convert_str_int(s, base = 2):
    return int(s,base)

def mutat_int(a):
    if (random()<mutation_rate):
        b = randint(0,8)        # defaultedd 8: unchangable
        s1 = pow(2,(abs(b-8+1)))
        s2 = pow(2,(abs(b-8)))-1
        m = pow(2,8)-1
        d = a - s1
        m2 = d & s2
        s3 = m - s2
        m1 = a & s3
        a = m1|m2
    return a

class DNA:
    def __init__(self,idx):
        self.idx = idx
        self.c_r = init_gene_int()
        self.c_g = init_gene_int()
        self.c_b = init_gene_int()


    def get_color(self):
        return (self.c_r, self.c_g, self.c_b)
        



def main():
    dna = DNA()
    print(dna.get_color())



if __name__=='__main__':
    main()
