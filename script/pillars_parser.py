import pandas as pd
from itertools import combinations
import numpy as np

def pillars_parser(FILE_PATH, ygob='all'):

    lg = len(ygob)
    if type(ygob) == list:
        if all(isinstance(x, int) for x in ygob):
            usecols = ygob
        else:
            print('ygob must be a list of column index (int)')
            return None
    else:
        usecols=None

    M = pd.read_csv(FILE_PATH, sep='\t', header = None, usecols=usecols)

    #print(M[M != '---'])

    M = M.where(M!='---', inplace=False).fillna(0)
    print(M.iloc[[0]])
    print(M.iloc[[4]])

    #print(M[[11,21]].all(axis=1))

    #print(pd.merge(M[[11]], M[[21]], how='inner'), on=[11,21])

    d = {}
    for i in range(lg):
        d[ygob[i]] = i
    print(d)

    c = np.zeros((lg,lg))
    for a,b in combinations(ygob,2):
        print(M[[a,b]].all(axis=1))
