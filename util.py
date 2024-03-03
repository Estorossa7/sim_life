from config import *

from random import randint, random

import numpy as np

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

#   cross over
def cross_over(m,f):
    b = randint(1,6)        # defaultedd 8: unchangable
    max = pow(2,8)-1
    s1 = pow(2,b)-1
    s2 = max - s1
    m1 = m & s2
    f1 = f & s2
    m2 = m & s1
    f2 = f & s1
    
    g1 = m1 | m2
    g2 = f1 | f2
    return g1, g2

#   mutation
def mutat_int(a):
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

#   fitness function
def fitness(dna):
    g = dna.get_color()
    t = target_color
    sum = 0
    for i in range(len(g)):
        sum += abs(g[i] - t[i])
    fit = sum
    return fit, g

#   order list
def get_order(l):
    s = np.array(l)
    sort_index = np.argsort(s)
    return list(sort_index)

#   get gene pool
def selection(l):
    l = sorted(l)
    return l

#   get parent pool
def mate(m,f):
    c1, c2 = [], []
    for i in range(len(m)):
        g1, g2 = cross_over(m[i],f[i])
        if(random()<mutation_rate):
            g1 = mutat_int(g1)
        if(random()<mutation_rate):
            g2 = mutat_int(g2)
        c1.append(g1)
        c2.append(g2)  
    return c1, c2