## Farm Household models code

import matplotlib.pyplot as plt
from ipywidgets import interact, fixed
import numpy as np
#plt.style.use('seaborn-whitegrid')
#from mpl_toolkits.mplot3d import *
#from matplotlib import cm
#from scipy.optimize import minimize


## Defautl parameters
ALPHA = 0.5
BETA = 0.7
TBAR = 100
LBAR = 100


## Technology and Preferences preferences

def F(T,L,alpha=ALPHA):
    return (T**alpha)*(L**(1-alpha))

def FL(T,L,alpha=ALPHA):
    """Shadow price of labor"""
    return (1-alpha)*F(T,L,alpha=ALPHA)/L

def FT(T,L,alpha=ALPHA):
    """Shadow price of labor"""
    return alpha*F(T,L,alpha=ALPHA)/T

def U(c, l, beta=BETA):
    return (c**beta)*(l**(1-beta))

def indif(l, ubar, beta=BETA):
    return ( ubar/(l**(1-beta)) )**(1/beta)

def leisure(Lbar,alpha=ALPHA, beta=BETA):
    a = (1-alpha)*beta/(1-beta)
    return Lbar/(1+a)

def HH(Tbar,Lbar,alpha=ALPHA, beta=BETA):
    """Household optimum leisure, consumption and utility"""
    a = (1-alpha)*beta/(1-beta)
    leisure = Lbar/(1+a)
    output = F(Tbar,Lbar-leisure, alpha)
    utility = U(output, leisure, beta)
    return leisure, output, utility 


## Farm optima (analytic solutions)

def farm_optimum(Tbar, w, alpha=ALPHA, beta=BETA):
    """returns optimal labor demand and profits"""
    LD = Tbar * ((1-alpha)/w)**(1/alpha)
    profit = F(Tbar, LD) - w*LD
    return LD, profit

def HH_optimum(Tbar, Lbar, w, alpha=ALPHA, beta=BETA):
    """returns optimal consumption, leisure and utility.
       Simple Cobb-Douglas choices from calculated income """
    _, profits = farm_optimum(Tbar, w, alpha)  
    income = profits + w*Lbar
    consumption = beta * income
    leisure = (1-beta) * income/w
    utility = U(consumption, leisure, beta)
    return consumption, leisure, utility



## plots

def chayanov(Tbar,Lbar,alpha=ALPHA, beta=BETA):
    leis = np.linspace(0.1,Lbar,num=100)
    q = F(Tbar,Lbar-leis,alpha)
    l_opt, Q, U = HH(Tbar, Lbar, alpha, beta)
    print("Leisure, Consumption, Utility =({:5.2f},{:5.2f},{:5.2f})"
          .format(l_opt, Q, U))
    print("shadow price labor:{:5.2f}".format(FL(Tbar,Lbar-l_opt,beta)))
    c = indif(leis,U,beta)
    fig, ax = plt.subplots(figsize=(8,8))
    ax.plot(leis, q, lw=2.5)
    ax.plot(leis, c, lw=2.5)
    ax.plot(l_opt,Q,'ob')
    ax.vlines(l_opt,0,Q, linestyles="dashed")
    ax.hlines(Q,0,l_opt, linestyles="dashed")
    ax.set_xlim(0, 110)
    ax.set_ylim(0, 150)
    ax.set_xlabel(r'$l - leisure$', fontsize=16)
    ax.set_ylabel('$c - consumption$', fontsize=16)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.grid()
    ax.set_title("Chayanovian Household Optimum")
    plt.show()


def plot_production(Tbar,Lbar, w, ax=None):
    if ax is None:
        ax = plt.gca()
    lei = np.linspace(1, Lbar)
    q = F(Tbar, Lbar-lei)
    ax.plot(lei, q, lw=2.5)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

def plot_farmconsumption(Tbar, Lbar, w, alpha=ALPHA, beta=BETA, ax=None):
    if ax is None:
        ax = plt.gca()
    lei = np.linspace(1, Lbar)
    LD, profits = farm_optimum(Tbar, w)
    q_opt = F(Tbar,LD)
    yline = profits + w*Lbar - w*lei
    c_opt, l_opt, u_opt = HH_optimum(Tbar, Lbar, w)
    
    ax.plot(Lbar-LD,q_opt,'ob') 
    ax.plot(lei, yline)  
    ax.plot(lei, indif(lei,u_opt, beta),'k')
    ax.plot(l_opt, c_opt,'ob')
    ax.vlines(l_opt,0,c_opt, linestyles="dashed")
    ax.hlines(c_opt,0,l_opt, linestyles="dashed")
    ax.vlines(Lbar - LD,0,q_opt, linestyles="dashed")
    ax.hlines(profits,0,Lbar, linestyles="dashed")
    ax.vlines(Lbar,0,F(Tbar,Lbar))
    ax.hlines(q_opt,0,Lbar, linestyles="dashed")
    ax.text(Lbar+1,profits,r'$\Pi ^*$',fontsize=16)
    ax.text(Lbar+1,q_opt,r'$F(\bar T, L^{*})$',fontsize=16)
    ax.text(-6,c_opt,r'$c^*$',fontsize=16)
    
    ax.annotate('',(Lbar-LD,2),(Lbar,2),arrowprops={'arrowstyle':'->'})
    ax.text((2*Lbar-LD)/2,3,r'$L^{*}$',fontsize=16)
    
    ax.text(l_opt/2,8,'$l^*$',fontsize=16)
    ax.annotate('',(0,7),(l_opt,7),arrowprops={'arrowstyle':'<-'})


