# -*- coding: utf-8 -*-
"""
A collection of functions to assist in shock relation calculations.
"""
from __future__ import division
from math import sqrt
import sqlite3 as lite

def isen_press_ratio(M, gam=1.4, P=None):
    '''
    Calculates the pressure ratio in an isentropic flow given the Mach number
    and specific heat ratio (default 1.4 for air).\n
    Parameters
    ------------------------
        M1 : float
            Incoming flow Mach number.
        gam : float, optional
            Specific heat ratio. Set to 1.4 by default (for air)\n
        P : float, optional
            Pressure. If known, the pressure may be given as the final argument
            which will return the total pressure.
    Returns
    ------------------------
        P0P : float
            Ratio of pressure to the total pressure (unless optional pressure
            argument is given, in which case the stagnation pressure
            alone is given).
    '''
    P0P = (1 + ((gam - 1)/2)*M*M)**(gam/(gam - 1))
    if P is None:
        return P0P
    return P*P0P

def isen_rho_ratio(M, gam=1.4, rho=None):
    '''
    Calculates the density ratio in an isentropic flow given the Mach number
    and specific heat ratio (default 1.4 for air).\n
    Parameters
    ------------------------
        M1 : float
            Incoming flow Mach number.
        gam : float, optional
            Specific heat ratio. Set to 1.4 by default (for air)\n
        rho : float, optional
            Density. If known, the density may be given as the final argument
            which will return the total density.
    Returns
    ------------------------
        rho0rho : float
            Ratio of density to the total density (unless optional density
            argument is given, in which case the stagnation density
            alone is given).
    '''
    rho0rho = (1 + ((gam - 1)/2)*M*M)**(1/(gam - 1))
    if rho is None:
        return rho0rho
    return rho*rho0rho

def isen_temp_ratio(M, gam=1.4, T=None):
    '''
    Calculates the temperature ratio in an isentropic flow given the Mach
    number and specific heat ratio (default 1.4 for air).\n
    Parameters
    ------------------------
        M1 : float
            Incoming flow Mach number.
        gam : float, optional
            Specific heat ratio. Set to 1.4 by default (for air)\n
        T : float, optional
            temperature. If known, the temperature may be given as the final
            argument which will return the total temperature.
    Returns
    ------------------------
        T0T : float
            Ratio of temperature to the total temperature (unless optional
            temperature argument is given, in which case the stagnation
            temperature alone is given).
    '''
    T0T = 1 + ((gam - 1)/2)*M*M
    if T is None:
        return T0T
    return T*T0T

def isen_area_ratio(M, gam=1.4, Astar=None):
    '''docstring
    '''
    AA = (1/(M*M))*((2/(gam + 1))*(1 + ((gam -\
    1)/2)*M*M))**((gam + 1)/(gam - 1))
    if not Astar is None:
        return sqrt(AA)/Astar
    return sqrt(AA)

def norm_mach2(M1, gam=1.4):
    '''
    Calculates the mach number after normal shock given the incoming mach.\n
    Parameters
    ------------------------
        M1 : float
            Incoming flow Mach number. Must be greater than 1 for shock.
        gam : float, optional
            Specific heat ratio. Set to 1.4 by default (for air)\n
    Returns
    ------------------------
        M2 : float
            Mach number of the flow directly after the shock
    '''
    M22 = (1 + ((gam - 1)/2)*M1*M1) / (gam*M1*M1 - (gam - 1)/2)
    return sqrt(M22)

def norm_rho_ratio(M1, gam=1.4, rho1=None):
    '''
    Calculates the density ratio before and after normal shock given the
    incoming mach. If the incoming density is given, than function returns a
    float value for the after shock density.\n
    Parameters
    ------------------------
        M1 : float
            Incoming flow Mach number. Must be greater than 1 for shock.
        gam : float, optional
            Specific heat ratio. Set to 1.4 by default (for air)
        rho1 : float, optional
            Density of the flow before the normal shock. If given, function
            returns a float value of the density after the shock.\n
    Returns
    ------------------------
        rho : float
            Ratio of the densities before and after shock (unless optional
            argument 'rho1' is specified, in which case 'rho' is the density
            after shock).
    '''
    rho2rho1 = ((gam + 1)*M1*M1) / (2 + (gam - 1)*M1*M1)
    if rho1 is None:
        return rho2rho1
    return rho1*rho2rho1

def norm_press_ratio(M1, gam=1.4, P1=None):
    '''
    Calculates the pressure ratio before and after normal shock given the
    incoming mach. If the incoming pressure is given, than function returns a
    float value for the after shock pressure.\n
    Parameters
    ------------------------
        M1 : float
            Incoming flow Mach number. Must be greater than 1 for shock.
        gam : float, optional
            Specific heat ratio. Set to 1.4 by default (for air)
        P1 : float, optional
            Pressure of the flow before the normal shock. If given, function
            returns a float value of the pressure after the shock.\n
    Returns
    ------------------------
        P : float
            Ratio of the pressures before and after shock (unless optional
            argument 'P1' is specified, in which case 'P' is the pressure
            after shock).
    '''
    P2P1 = 1 + (2*gam/(gam + 1))*(M1*M1 - 1)
    if P1 is None:
        return P2P1
    return P1*P2P1

def norm_temp_ratio(M1, gam=1.4, T1=None):
    '''
    Calculates the temperature ratio before and after normal shock given the
    incoming mach. If the incoming temp is given, than function returns a
    float value for the after shock temperature.\n
    Parameters
    ------------------------
        M1 : float
            Incoming flow Mach number. Must be greater than 1 for shock.
        gam : float, optional
            Specific heat ratio. Set to 1.4 by default (for air)
        T1 : float, optional
            Temperature of the flow before the normal shock. If given, function
            returns a float value of the temperature after the shock.\n
    Returns
    ------------------------
        T : float
            Ratio of the temperatures before and after shock (unless optional
            argument 'T1' is specified, in which case 'T' is the temperature
            after shock).
    '''
    T2T1 = (1 + (2*gam/(gam + 1))*(M1*M1 - 1))*(2 +\
    (gam - 1)*M1*M1)/((gam + 1)*M1*M1)
    if T1 is None:
        return T2T1
    return T1*T2T1


def loc_speed_sound(T, gam=1.4, R=287):
    '''
    Local speed of sound\n
    Parameters
    ------------------------
        T : float
            Temperature (in Kelvin if using the default gas constant)
        gam : float, optional
            Specific heat ratio. Set to 1.4 by default (for air)
        R : float, optional
            Universal gas constant. 287 J/(kg K) by default
    Returns
    ------------------------
        a : float
            Local speed of sound in m/s (if using default units)
    '''
    a = sqrt(gam*R*T)
    return a

def tablelookup(table=None, col1=None, value=None, col2=None, db=None):
    '''
    Interpolates a value from the gas tables.
    '''
    if db is None:
        gastables = lite.connect('gastables.db')
    else:
        gastables = db
    with gastables:
        gastables.row_factory = lite.Row
        cur = gastables.cursor()
        if table is None:
            cur.execute("SELECT name FROM SQLITE_MASTER WHERE TYPE = 'table'")
            return [a['name'] for a in cur.fetchall()]
        cur.execute('SELECT * FROM %s' % table)
        keys = [k.lower() for k in cur.fetchone().keys()][1:]
        if col1 is None:
            return cur.fetchone().keys()[1:]
        elif value is None:
            print 'Must input value to lookup'
        else:
            if 'aastar' in col1.lower():
                tups = (('>=', 'AND M > 1'), ('<=', 'AND M > 1'),\
                ('<=', 'AND M < 1'), ('>=', 'AND M < 1'))
            else:
                tups = (('>=', ''), ('<=', ''))
            rs = []
            for tup in tups:
                sh = '''SELECT * FROM {0}
                WHERE {1} %s {2} %s
                ORDER BY ABS({1} - {2})
                LIMIT 1''' % tup
                cur.execute(sh.format(table, col1, value))
                rs += cur.fetchall()
            ret = []
            rs.sort(key=lambda k: k['id'])
            for c in range(0, len(rs), 2):
                if not rs[c][col1] == rs[c + 1][col1]:
                    interp = (value - \
                    rs[c][col1])/(rs[c + 1][col1] - rs[c][col1])
                else:
                    interp = 0
                ret += [[interp*(a[1] - a[0]) + a[0] for a in\
                zip(rs[c], rs[c + 1])][1:]]
            if col2 is None:
                return ret
            return [val[keys.index(col2.lower())] for val in ret]

def table_generator(gamma, R):
    pass