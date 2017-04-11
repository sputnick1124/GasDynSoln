# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 11:00:02 2015

@author: nick
"""
from __future__ import division
from shock import *

# <codecell> Problem 1
#==============================================================================
# A normal shock is moving at 520 m/s into still air (300 K, 1 atm, gamma=1.4)
# Find the temperature behind the shock after the shock passes and the velocity
# of the gas behind the shock.
#==============================================================================
T1 = 300
u1 = 520
P1 = 1.0135e5
a1 = loc_speed_sound(T1)
M1 = u1/a1
T2 = norm_temp_ratio(M1, T1=T1)
M2 = norm_mach2(M1)
a2 = loc_speed_sound(T2)
u2 = a2*M2
print('T2=%3.0fK, u2=%3.0fm/s' % (T2, u2))
# <codecell> Problem 2
#==============================================================================
# Air flows through a frictionless adiabatic conrging-diverging nozzle. The air
# (gamma=1.4) stagnation pressure and temperature are 70e5 Pa and 500 K,
# respectively. The diverging portion of the nozzle has an area ratio of 11.91.
# A normal shock wave stands in the diverging section where the Mach number is
# 3.0. Calculate the Mach number and the static temperature and pressure in the
# nozzle exit plane
#==============================================================================
P01 = 7e5
T0 = 500
M1 = 3
AeA1star = 11.91

T0T = isen_temp_ratio(M1)
T1 = T0*1/T0T
A1Astar = isen_area_ratio(M1)

M2 = norm_mach2(M1)
A2Astar = isen_area_ratio(M2)
T2T1 = norm_temp_ratio(M1)
T2 = T2T1*T1

P02P01 = tablelookup('shock','M1',3,'p02p01')[0]
A1starA2star = P02P01
AeA2star = A1starA2star*AeA1star

Me,P02Pe,_,T0Te,_ = tablelookup('isentropic','aastar',AeA2star)[0]

Pe = P01*P02P01/P02Pe
Te = T0/T0Te
print('Me=%0.2f, Te=%3.0fK, Pe=%3.0fPa' % (Me,Te,Pe))
# <codecell> Problem 3
#==============================================================================
# An airstream at Mach 2 with pressure of 100e3 Pa and temerature of 270 K
# enters a diverging channel with a ratio of exit to inlet area of 3.0.
# Determine the back pressure necessary to produce a normal shock in the
# channel at an area equal to twice the inlet area. Assume one-dimensional
# steady flow with the behaving as a perfect as with constant specific heats.
# Also, assume that the flow can be considered as an isentropic flow except for
# the normal shock.
#==============================================================================
Pi = 100e3
Ti = 270
Mi = 2
A1Ai = 2
AeAi = 3

AiAstar = isen_area_ratio(Mi)
A1Astar = AiAstar*A1Ai

M1 = tablelookup('isentropic','aastar',A1Astar,'m')[1]
M2 = norm_mach2(M1)

A2Astar = isen_area_ratio(M2)
AeA2 = AeAi/A1Ai
AeAstar = AeA2*A2Astar

A2starA1star = AeAi*AiAstar*1/AeAstar

P0Pi = isen_press_ratio(2)
P01 = Pi*P0Pi

P02 = P01*1/A2starA1star
Me = tablelookup('isentropic','Aastar',AeAstar,'m')[0]

P0Pe = isen_press_ratio(Me)
Pe = P02/P0Pe
print('Pe=%3.0fPa' % Pe)