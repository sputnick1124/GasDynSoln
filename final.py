#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

from shock import * #imports all of the isentropic functions and lookuptable

#Problem 3
Mi = 2.8    #mach
Pi = 130e3  #Pa
Ti = 320    #K

A1Ai = np.arange(1.5,4.75,0.25)

#NB: we could explicitly define gamma=1.4, but all of the functions assume this
#anyway, so no need.

#We know A1/Ai (given in problem statement), and we can find out Ai/Astar (from
#either the equation or lookuptable), so A1/Astar is just the product. Once we
#have that, then we can lookup M1 (mach right before shock) for each A1/Ai and
#go from there.

AiAstar = isen_area_ratio(Mi)
A1Astar = AiAstar*A1Ai

#now get M1 right before shock by lookup on A1Astar. Since there are two input
#Mach numbers which can produce any A/Astar ratio, we take the second one which
#corresponds to a supersonic input flow. (i.e. index '1' from tablelookup return)
M1 = np.array([tablelookup('isentropic','AAstar',aa,'M')[1] for aa in A1Astar])

#now we just need to get the back pressure by multiplying through the pressure
#ratios at every step. More than one option here, but we'll use
#Pe = Pi*P01/Pi*P02/P01*(P02/Pe)^-1
M2 = np.array([norm_mach2(m) for m in M1])
P01Pi = isen_press_ratio(Mi)
P02P01 = np.array([tablelookup('shock','M1',m,'P02P01')[0] for m in M1])
P02Pe = np.array([tablelookup('isentropic','M',m,'P0P')[0] for m in M2])

Pe = Pi*P01Pi*P02P01*(1/P02Pe)

#now we need to recover Me by getting a final set of area ratios from M2 etc.
#essentially find Ae/A2star and use it (via lookup) to get Me
AeAi = 5 #from problem statement
A1A2star = np.array([tablelookup('isentropic','M',m,'AAstar')[0] for m in M2])
A2starA1star = AiAstar*A1Ai*(1/A1A2star)
AeA2star = AeAi*AiAstar*(1/A2starA1star)
Me = np.array([tablelookup('isentropic','AAstar',aa,'M')[0] for aa in AeA2star])

#Plot the first things
#two y-axes code ripped from http://matplotlib.org/examples/api/two_scales.html
fig, ax1 = plt.subplots()
ax1.plot(A1Ai, Pe/1e3, 'bo-') #divide by 1000 to get kPa from Pa
ax1.set_xlabel('Shock location at $\\frac{A_1}{A_i}$')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('$P_b$ (kPa)', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(A1Ai, Me, 'r*-')
ax2.set_ylabel('$M_e$', color='r')
ax2.tick_params('y', colors='r')
plt.show()


#On to the second part. Show how mach varies through the nozzle
#We already have everything we need for this. No need to compute intermediate
#values since Mach varies linearly as it traverses an isentropic nozzle

#we do need to reformat our data slightly
Mis = Mi*np.ones(M1.shape[0])
M = np.vstack((Mis,M1,M2,Me))

#plot the next things
plt.figure()
plt.plot([1,2,3,4],M)
plt.legend([str(x) for x in A1Ai],title='$\\frac{A_1}{A_i}$')
x = [1,2,3,4]
xlabels = ['$A_i$','$A_1$','$A_2$','$A_e$']
plt.xlabel('Station in nozzle')
plt.ylabel('Mach number')
plt.xticks(x,xlabels)