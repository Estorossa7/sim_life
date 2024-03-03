from config import *

from random import randint, random

import numpy as np
import pandas as pd
import os

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
    s3 = pow(2,abs(b-8))-1
    s4 = max - s3

    m1 = m & s2
    f1 = f & s2
    m2 = m & s1
    f2 = f & s1
    
    m3 = m & s4
    f3 = f & s4
    m4 = m & s3
    f4 = f & s3
    
    g1 = m1 | f2
    g2 = f1 | m2
    g3 = m3 | f4
    g4 = f3 | m4
    return [g1, g2, g3, g4]

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
def fitness(dna, target_color):
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
    c = []
    for i in range(len(m)):
        g = cross_over(m[i],f[i])
        for i in g:
            if(random()<mutation_rate):
                i = mutat_int(i)
        c.append(g)
    c = np.array(c)
    c = c.transpose()
    return c


#   write to dataframe
def write_file(l1, l2, iter, gen):
    dic = {'color': l1, 'fitness': l2}
    df = pd.DataFrame.from_dict(dic)
    path = save_genes + str(iter) + '\\' + str(gen) + '.csv'
    df.to_csv(path,index=False)

