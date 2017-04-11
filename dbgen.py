# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 12:34:44 2015

@author: nick
"""

import sqlite3 as lite

gas = lite.connect('gastables.db')

with gas:
    cur = gas.cursor()
    cur.execute('DROP TABLE IF EXISTS Isentropic')
    cur.execute('CREATE TABLE Isentropic(ID INT, M FLOAT, P0P FLOAT, rho0rho FLOAT, T0T FLOAT, AAstar FLOAT)')
    with open('gastables/isentropicTables/isenTable.txt','r') as isen:
        isendata = isen.readlines()
        c = 1
        for line in isendata:
            cur.execute('INSERT INTO Isentropic VALUES(?,?,?,?,?,?)',[c]+[float(item[:-3]+'e'+item[-3:]) for item in line.split()])
            c += 1
    
    cur.execute('DROP TABLE IF EXISTS Shock')
    cur.execute('CREATE TABLE Shock(ID INT, M1 FLOAT, P2P1 FLOAT, rho2rho1 FLOAT, T2T1 FLOAT, P02P01 FLOAT, P02P1 FLOAT, M2 FLOAT)')
    with open('gastables/shockTables/shockTable.txt','r') as shock:
        shockdata = shock.readlines()
        c = 1
        for line in shockdata:
            cur.execute('INSERT INTO Shock VALUES(?,?,?,?,?,?,?,?)',[c]+[float(item[:-3]+'e'+item[-3:]) for item in line.split()])
            c += 1
