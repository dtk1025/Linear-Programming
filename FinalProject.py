#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 21:43:40 2021

@author: deez
"""

"""objective"""

import pulp as p
import pandas as pd

model = p.LpProblem('myproblem', p.LpMaximize)

#ad expenses per period
aw1 = p.LpVariable('aw1', lowBound=0) 
ag1 = p.LpVariable('ag1', lowBound=0)
af1 = p.LpVariable('af1', lowBound=0)

aw2 = p.LpVariable('aw2', lowBound=0) 
ag2 = p.LpVariable('ag2', lowBound=0)
af2 = p.LpVariable('af2', lowBound=0)

aw3 = p.LpVariable('aw3', lowBound=0) 
ag3 = p.LpVariable('ag3', lowBound=0)
af3 = p.LpVariable('af3', lowBound=0)

aw4 = p.LpVariable('aw4', lowBound=0) 
ag4 = p.LpVariable('ag4', lowBound=0)
af4 = p.LpVariable('af4', lowBound=0)

aw5 = p.LpVariable('aw5', lowBound=0) 
ag5 = p.LpVariable('ag5', lowBound=0)
af5 = p.LpVariable('af5', lowBound=0)

#production by product by period by factory
#widget

pw1a = p.LpVariable('pw1a', lowBound=0) 
pw2a = p.LpVariable('pw2a', lowBound=0) 
pw3a = p.LpVariable('pw3a', lowBound=0) 
pw4a = p.LpVariable('pw4a', lowBound=0) 
pw5a = p.LpVariable('pw5a', lowBound=0) 

pw1b = p.LpVariable('pw1b', lowBound=0) 
pw2b = p.LpVariable('pw2b', lowBound=0) 
pw3b = p.LpVariable('pw3b', lowBound=0) 
pw4b = p.LpVariable('pw4b', lowBound=0) 
pw5b = p.LpVariable('pw5b', lowBound=0) 

#gadget

pg1a = p.LpVariable('pg1a', lowBound=0) 
pg2a = p.LpVariable('pg2a', lowBound=0) 
pg3a = p.LpVariable('pg3a', lowBound=0) 
pg4a = p.LpVariable('pg4a', lowBound=0) 
pg5a = p.LpVariable('pg5a', lowBound=0) 

pg1b = p.LpVariable('pg1b', lowBound=0) 
pg2b = p.LpVariable('pg2b', lowBound=0) 
pg3b = p.LpVariable('pg3b', lowBound=0) 
pg4b = p.LpVariable('pg4b', lowBound=0) 
pg5b = p.LpVariable('pg5b', lowBound=0) 

#flugel

pf1a = p.LpVariable('pf1a', lowBound=0) 
pf2a = p.LpVariable('pf2a', lowBound=0) 
pf3a = p.LpVariable('pf3a', lowBound=0) 
pf4a = p.LpVariable('pf4a', lowBound=0) 
pf5a = p.LpVariable('pf5a', lowBound=0) 

pf1b = p.LpVariable('pf1b', lowBound=0) 
pf2b = p.LpVariable('pf2b', lowBound=0) 
pf3b = p.LpVariable('pf3b', lowBound=0) 
pf4b = p.LpVariable('pf4b', lowBound=0) 
pf5b = p.LpVariable('pf5b', lowBound=0) 

#ship per production per period per factory

tw1a = p.LpVariable('tw1a', lowBound=0) 
tw2a = p.LpVariable('tw2a', lowBound=0) 
tw3a = p.LpVariable('tw3a', lowBound=0) 
tw4a = p.LpVariable('tw4a', lowBound=0) 
tw5a = p.LpVariable('tw5a', lowBound=0) 

tw1b = p.LpVariable('tw1b', lowBound=0) 
tw2b = p.LpVariable('tw2b', lowBound=0) 
tw3b = p.LpVariable('tw3b', lowBound=0) 
tw4b = p.LpVariable('tw4b', lowBound=0) 
tw5b = p.LpVariable('tw5b', lowBound=0) 

#gadget
tg1a = p.LpVariable('tg1a', lowBound=0) 
tg2a = p.LpVariable('tg2a', lowBound=0) 
tg3a = p.LpVariable('tg3a', lowBound=0) 
tg4a = p.LpVariable('tg4a', lowBound=0) 
tg5a = p.LpVariable('tg5a', lowBound=0) 

tg1b = p.LpVariable('tg1b', lowBound=0) 
tg2b = p.LpVariable('tg2b', lowBound=0) 
tg3b = p.LpVariable('tg3b', lowBound=0) 
tg4b = p.LpVariable('tg4b', lowBound=0) 
tg5b = p.LpVariable('tg5b', lowBound=0) 

#flugel
tf1a = p.LpVariable('tf1a', lowBound=0) 
tf2a = p.LpVariable('tf2a', lowBound=0) 
tf3a = p.LpVariable('tf3a', lowBound=0) 
tf4a = p.LpVariable('tf4a', lowBound=0) 
tf5a = p.LpVariable('tf5a', lowBound=0) 

tf1b = p.LpVariable('tf1b', lowBound=0) 
tf2b = p.LpVariable('tf2b', lowBound=0) 
tf3b = p.LpVariable('tf3b', lowBound=0) 
tf4b = p.LpVariable('tf4b', lowBound=0) 
tf5b = p.LpVariable('tf5b', lowBound=0) 

#raw material per type (a,b) per period per plant
ra1a = p.LpVariable('ra1a', lowBound=0) 
ra2a = p.LpVariable('ra2a', lowBound=0) 
ra3a = p.LpVariable('ra3a', lowBound=0) 
ra4a = p.LpVariable('ra4a', lowBound=0) 
ra5a = p.LpVariable('ra5a', lowBound=0) 

ra1b = p.LpVariable('ra1b', lowBound=0) 
ra2b = p.LpVariable('ra2b', lowBound=0) 
ra3b = p.LpVariable('ra3b', lowBound=0) 
ra4b = p.LpVariable('ra4b', lowBound=0) 
ra5b = p.LpVariable('ra5b', lowBound=0)

rb1a = p.LpVariable('rb1a', lowBound=0) 
rb2a = p.LpVariable('rb2a', lowBound=0) 
rb3a = p.LpVariable('rb3a', lowBound=0) 
rb4a = p.LpVariable('rb4a', lowBound=0) 
rb5a = p.LpVariable('rb5a', lowBound=0) 

rb1b = p.LpVariable('rb1b', lowBound=0) 
rb2b = p.LpVariable('rb2b', lowBound=0) 
rb3b = p.LpVariable('rb3b', lowBound=0) 
rb4b = p.LpVariable('rb4b', lowBound=0) 
rb5b = p.LpVariable('rb5b', lowBound=0)

#labor per period per plant
l1a = p.LpVariable('l1a', lowBound=0) 
l2a = p.LpVariable('l2a', lowBound=0) 
l3a = p.LpVariable('l3a', lowBound=0) 
l4a = p.LpVariable('l4a', lowBound=0) 
l5a = p.LpVariable('l5a', lowBound=0) 

l1b = p.LpVariable('l1b', lowBound=0) 
l2b = p.LpVariable('l2b', lowBound=0) 
l3b = p.LpVariable('l3b', lowBound=0) 
l4b = p.LpVariable('l4b', lowBound=0) 
l5b = p.LpVariable('l5b', lowBound=0) 

#labor overtime
lo1a = p.LpVariable('lo1a', lowBound=0) 
lo2a = p.LpVariable('lo2a', lowBound=0) 
lo3a = p.LpVariable('lo3a', lowBound=0) 
lo4a = p.LpVariable('lo4a', lowBound=0) 
lo5a = p.LpVariable('lo5a', lowBound=0) 

lo1b = p.LpVariable('lo1b', lowBound=0) 
lo2b = p.LpVariable('lo2b', lowBound=0) 
lo3b = p.LpVariable('lo3b', lowBound=0) 
lo4b = p.LpVariable('lo4b', lowBound=0) 
lo5b = p.LpVariable('lo5b', lowBound=0) 

#inventory/storage
#widget
sw1a = p.LpVariable('sw1a', lowBound=0) 
sw2a = p.LpVariable('sw2a', lowBound=0) 
sw3a = p.LpVariable('sw3a', lowBound=0) 
sw4a = p.LpVariable('sw4a', lowBound=0) 
sw5a = p.LpVariable('sw5a', lowBound=0) 

sw1b = p.LpVariable('sw1b', lowBound=0) 
sw2b = p.LpVariable('sw2b', lowBound=0) 
sw3b = p.LpVariable('sw3b', lowBound=0) 
sw4b = p.LpVariable('sw4b', lowBound=0) 
sw5b = p.LpVariable('sw5b', lowBound=0) 

#gadget
sg1a = p.LpVariable('sg1a', lowBound=0) 
sg2a = p.LpVariable('sg2a', lowBound=0) 
sg3a = p.LpVariable('sg3a', lowBound=0) 
sg4a = p.LpVariable('sg4a', lowBound=0) 
sg5a = p.LpVariable('sg5a', lowBound=0) 

sg1b = p.LpVariable('sg1b', lowBound=0) 
sg2b = p.LpVariable('sg2b', lowBound=0) 
sg3b = p.LpVariable('sg3b', lowBound=0) 
sg4b = p.LpVariable('sg4b', lowBound=0) 
sg5b = p.LpVariable('sg5b', lowBound=0) 

#flugels
sw1a = p.LpVariable('sw1a', lowBound=0) 
sw2a = p.LpVariable('sw2a', lowBound=0) 
sw3a = p.LpVariable('sw3a', lowBound=0) 
sw4a = p.LpVariable('sw4a', lowBound=0) 
sw5a = p.LpVariable('sw5a', lowBound=0) 

sw1b = p.LpVariable('sw1b', lowBound=0) 
sw2b = p.LpVariable('sw2b', lowBound=0) 
sw3b = p.LpVariable('sw3b', lowBound=0) 
sw4b = p.LpVariable('sw4b', lowBound=0) 
sw5b = p.LpVariable('sw5b', lowBound=0) 

"""
pw1a = p.LpVariable('pw1a', lowBound=0)- prod
aw1 = p.LpVariable('aw1', lowBound=0) - ad
sw1a = p.LpVariable('sw1a', lowBound=0) - tra
l1a = p.LpVariable('l1a', lowBound=0)  - lab
ra1a = p.LpVariable('ra1a', lowBound=0)  - raw mat

"""


#objective

model += (2490*pw1a + 2490*pw1b + 2490*pw2a + 2490*pw2b + 2490*pw3a + 2490*pw3b + 2490*pw4a + 2490*pw4b + 2490*pw5a + 2490*pw5b 
+ 1990*pg1a + 1990*pg1b + 1990*pg2a + 1990*pg2b + 1990*pg3a + 1990*pg3b + 1990*pg4a + 1990*pg4b + 1990*pg5a + 1990*pg5b 
+ 2970*pf1a + 2970*pf1b + 2970*pf2a + 2970*pf2b + 2970*pf3a + 2970*pf3b + 2970*pf4a + 2970*pf4b + 2970*pf5a + 2970*pf5b) 
- (aw1 + aw2 + aw3 + aw4 + aw5 + ag1 + ag2 + ag3 + ag4 + ag5 + af1 + af2+ af3 + af4 + af5)
- (1.25*ra1a + 2.65*ra1b + 1.45*rb1a  + 2.9*rb1b  + 1.25*ra2a + 2.65*ra2b + 1.45*rb2a  + 2.9*rb2b + 1.25*ra3a + 2.65*ra3b + 1.45*rb3a  + 2.9*rb3b + 1.25*ra4a + 2.65*ra4b + 1.45*rb4a  + 2.9*rb4b + 1.25*ra5a + 2.65*ra5b + 1.45*rb5a  + 2.9*rb5b)
- (11*l1a + 11*l1b + 11*l2a + 11*l2b + 1.05*11*l3a + 1.1*11*l3b + 1.05*11*l4a + 1.1*11*l4b + 1.05*11*l4a + 1.1*11*l4b + 1.05*11*l5a + 1.1*11*l5b + 16.5*lo1a + 16.5*lo1b + 16.5*lo2a + 16.5*lo2b + 1.05*16.5*lo3a + 1.1*16.5*lo3b + 1.05*16.5*lo4a + 1.1*16.5*lo4b + 1.05*16.5*lo5a + 1.1*16.5*lo5b 
- (7.5*sw1a + 7.8*sw1b + 7.5*sw2a + 7.8*sw2b + 7.5*sw3a + 7.8*sw3b + 7.5*sw4a + 7.8*sw4b + 7.5*sw5a + 7.8*sw5b + 5.5*sg1a + 5.7*sg1b + 5.5*sg2a + 5.5*sg2b + 5.7*sg3a + 5.5*sw3b + 5.7*sw4a + 5.5*sw4b + 5.7*sw5a + 5.5*sw5b + 6.5*sf1a + 7*sf1b + 6.5*sf2a + 7*sf2b + 6.5*sf3a + 7*sf3b + 6.5*sf4a + 7*sf4b + 6.5*sf5a + 7*swfb)
- (6.3*tw1a + 6.5*tw1b + 6.3*tw2a + 6.3*tw2b + 6.3*tw3a + 6.3*tw3b + 6.3*tw4a + 6.3*tw4b + 6.3*tw5a + 6.3*tw5b + 4.6*tg1a + 5*tg1b + 4.6*tg2a + 5*tg2b + 4.6*tg3a + 5*tg3b + 4.6*tg4a + 5*tg4b + 4.6*tg5a + 5*tg5b + 5.5*tf1a + 5.7*tf1b + 5.5*tf2a + 5.7*tf2b + 5.5*tf3a + 5.7*tf3b + 5.5*tf4a + 5.7*tf4b + 5.5*tf5a + 5.7*tf5b)
)

#constraints
model += ra1a + ra2a <=140000
model += 194*pw1a + 230*pg1a + 178*pf1a <= ra1a
model += 194*pw2a + 230*pg2a + 178*pf2a <= ra2a
model += 194*pw3a + 230*pg3a + 178*pf3a <= ra3a
model += 194*pw4a + 230*pg4a + 178*pf4a <= ra4a
model += 194*pw5a + 230*pg5a + 178*pf5a <= ra5a

model += 188*pw1a + 225*pg1a + 170*pf1a <= ra1b
model += 188*pw2a + 225*pg2a + 170*pf2a <= ra2b
model += 188*pw3a + 225*pg3a + 170*pf3a <= ra3b
model += 188*pw4a + 225*pg4a + 170*pf4a <= ra4b
model += 188*pw5a + 225*pg5a + 170*pf5a <= ra5b

model += ra1a + ra1b <= 140000
model += ra2a + ra2b <= 140000
model += ra3a + ra3b <= 140000
model += ra4a + ra4b <= 140000
model += ra5a + ra5b <= 140000

model += 8.6*pw1a + 0*pg1a + 11.6*pf1a <= rb1a
model += 8.6*pw2a + 0*pg2a + 11.6*pf2a <= rb2a
model += 8.6*pw3a + 0*pg3a + 11.6*pf3a <= rb3a
model += 8.6*pw4a + 0*pg4a + 11.6*pf4a <= rb4a
model += 8.6*pw5a + 0*pg5a + 11.6*pf5a <= rb5a

model += 9.2*pw1a + 0*pg1a + 10.8*pf1a <= rb1b
model += 9.2*pw2a + 0*pg2a + 10.8*pf2a <= rb2b
model += 9.2*pw3a + 0*pg3a + 10.8*pf3a <= rb3b
model += 9.2*pw4a + 0*pg4a + 10.8*pf4a <= rb4b
model += 9.2*pw5a + 0*pg5a + 10.8*pf5a <= rb5b

model += rb1a + rb1b <= 5000
model += rb2a + rb2b <= 5000
model += rb3a + rb3b <= 5000
model += rb4a + rb4b <= 5000
model += rb5a + rb5b <= 5000

model += 9.5*pw1a + 7.1*pg1a + 11.1*pf1a <= l1a + lo1a
model += 9.5*pw2a + 7.1*pg2a + 11.1*pf2a <= l2a + lo2a
model += 9.5*pw3a + 7.1*pg3a + 11.1*pf3a <= l3a + lo3a
model += 9.5*pw4a + 7.1*pg4a + 11.1*pf4a <= l4a + lo4a
model += 9.5*pw5a + 7.1*pg5a + 11.1*pf5a <= l5a + lo5a

model += l1a <= 2500
model += l2a <= 2500
model += l3a <= 2500
model += l4a <= 2500
model += l5a <= 2500

model += 9.1*pw1b + 7.8*pg1b + 10.6*pf1b <= l1b + lo1b
model += 9.1*pw2b + 7.8*pg2b + 10.6*pf2b <= l2b + lo2b
model += 9.1*pw3b + 7.8*pg3b + 10.6*pf3b <= l3b + lo3b
model += 9.1*pw4b + 7.8*pg4b + 10.6*pf4b <= l4b + lo4b
model += 9.1*pw5b + 7.8*pg5b + 10.6*pf5b <= l5b + lo5b

model += l1b <= 3800
model += l2b <= 3800
model += l3b <= 3800
model += l4b <= 3800
model += l5b <= 3800

model += sw1a + sg1a + sf1a <= 70
model += sw2a + sg2a + sf2a <= 70
model += sw3a + sg3a + sf3a <= 70
model += sw4a + sg4a + sf4a <= 70
model += sw5a + sg5a + sf5a <= 70

model += sw1b + sg1b + sf1b <= 50
model += sw2b + sg2b + sf2b <= 50
model += sw3b + sg3b + sf3b <= 50
model += sw4b + sg4b + sf4b <= 50
model += sw5b + sg5b + sf5b <= 50

#check
model += pw1a - tw1a = sw1a
model += tw1a + pw2a - tw2a = sw2a
model += tw2a + pw3a - tw3a = sw3a
model += tw3a + pw4a - tw4a = sw4a
model += tw4a + pw5a - tw5a = sw5a

model += pw1b - tw1b = sw1b
model += tw1b + pw2b - tw2b = sw2b
model += tw2b + pw3b - tw3b = sw3b
model += tw3b + pw4b - tw4b = sw4b
model += tw4b + pw5b = sw5b

model += pg1a - tg1a = sg1a
model += tg1a + pg2a - tg2a = sg2a
model += tg2a + pg3a - tg3a = sg3a
model += tg3a + pg4a - tg4a = sg4a
model += tg4a + pg5a - tg5a = sg5a

model += pg1b - tg1b = sg1b
model += tg1b + pg2b - tg2b = sg2b
model += tg2b + pg3b - tg3b = sg3b
model += tg3b + pg4b - tg4b = sg4b
model += tg4b + pg5b = sg5b

model += pf1a - tf1a = sf1a
model += tf1a + pf2a - tf2a = sf2a
model += tf2a + pf3a - tf3a = sf3a
model += tf3a + pf4a - tf4a = sf4a
model += tf4a + pf5a - tf5a = sf5a

model += pf1b - tf1b = sf1b
model += tf1b + pf2b - tf2b = sf2b
model += tf2b + pf3b - tf3b = sf3b
model += tf3b + pf4b - tf4b = sf4b
model += tf4b + pf5b = sf5b


model.solve()

print('Model Status: {}'.format(p.LpStatus[model.status]))
print('Objective = ', p.value(model.objective))

for v in model.variables():
    print(v.name, '-', v.varValue, "\tReduced Cost=", v.dj)
    
s = [{'name': name, 'Shadow Price': c.pi, 
      'Slack': c.slack} for name, c in model.constraints.items()]
print(pd.DataFrame(s))
