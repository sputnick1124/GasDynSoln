# -*- coding: utf-8 -*-

import os
tabdir = os.path.join(os.getcwd(),'gastables')
isendir = os.path.join(tabdir,'isentropicTables')
shockdir = os.path.join(tabdir,'shockTables')
isentabs = os.listdir(isendir)
shocktabs = os.listdir(shockdir)
isendata, shockdata = [], []
for tab in sorted(isentabs):
    with open(os.path.join(isendir,tab),'r') as infile:
        isendata += infile.readlines()
for tab in sorted(shocktabs):
    with open(os.path.join(shockdir,tab),'r') as infile:
        shockdata += infile.readlines()

dirs = (isendir, shockdir)
data = (isendata, shockdata)
fnames = ('isenTable.txt','shockTable.txt')
for path, dataset, ofile in zip(dirs, data, fnames):
    with open(os.path.join(path,ofile),'w') as outfile:
        for line in dataset:
            outfile.write('\t'.join(line.strip().split()) + '\n')