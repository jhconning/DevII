# -*- coding: utf-8 -*-
""" geqfarm.py   General Equilibrium Farm Size Distribution

*** This version in mir-economy repo ***

Author: Jonathan Conning
An Economy Class and methods for calculating and representing General
equilibrium models of the farm size distribution with and without factor
market distortions.
Authors: Jonathan Conning & Aleks Michuda
"""
#%%
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import minimize
from collections import namedtuple

#%%
class Economy(object):

    """  Economy with an Equilibrium Farm Size Distribution
    Args:
         N (int): number of farm-size classes or bins in the distribution
    Examples:
        To solve for a competitive equilibrium with 5 farmer classes each with one
        unit of skill.
        >>> E = Economy(5)
        >>> E.smallhold_eq([100,100],E.s)
        result(w=array([ 0.21971211,  0.21971211]),
        X=array([[ 20.,  20.,  20.,  20.,  20.], [ 20.,  20.,  20.,  20.,  20.]]))
        To solve for the market-power distorted equilibrium with THETA = 0.8
        >>> E.cartel_eq(0.85)
        result(w=array([ 0.2734677,  0.1954175]),
        X=array([[ 13.11157595,  13.11157595,  13.11157595,  13.11157595, 47.55369619],
        [ 18.34836944,  18.34836944,  18.34836944,  18.34836944, 26.60652225]]))
    Note:
        We take the landlord class to be last [-1] indexed group.
        By default the initial distribution of skills is uniformly distributed.
        For example N = 5 and s = np.array([1, 1, 1, 1, 1.5]) has 5 farmer groups.
        But any distribution can be used.
    """

    def __init__(self, N):  # constructor to set initial default parameters.
        self.N       = N   # of xtiles (number of skill groups)
        self.GAMMA   = 0.98   # homogeneity factor; set high for close to CRS in F(T,L)
        self.ALPHA   = 0.5    # alpha (land) for production function
        self.LAMBDA  = 1.0/N  # landlord share of labor
        self.TBAR    = 100    # Total Land Endowment
        self.LBAR    = 100    # Total Labor Endowment
        self.H       = 0.0    # fixed cost of production
        self.s       = np.ones(N)
        self.Lucas   = False
        self.analytic= True  #solve CD analytically if true

    def __repr__(self):
        return 'Economy(N={}, GAM={}, TBAR={}, LBAR={})'.format(self.N, self.GAMMA, self.TBAR, self.LBAR)

    def prodn(self, X, s):
        """
        Production function
        Args:
            X:  vector of factor inputs (X[0] land and X[1] labor)
            s:  vector of skill endowments by xtile
        Returns:  vector of output(s)
        """
        T, L = X
        Y = s**(1-self.GAMMA) * ((T**self.ALPHA)*(L**(1-self.ALPHA)))**self.GAMMA
        return Y

    def prodn0(self, X, s):
        """
        Production function
        Args:
            X:  vector of factor inputs (X[0] land and X[1] labor)
            s:  vector of skill endowments by xtile
        Returns:  vector of output(s)
        """
        T, L = X
        Y = s * ((T**self.ALPHA)*(L**(1-self.ALPHA)))**self.GAMMA
        return Y

    def marginal_product(self, X, s):
        """
        Factor marginal products fo Cobb-Douglas
        Args:
            X:  vector of factor inputs (X[0] land and X[1] labor)
            s:  vector of skill endowments by xtile
        Returns:  vector of marginal products
        """
        T, L = X
        MPT = self.ALPHA * self.GAMMA * self.prodn(X,  s)/T
        MPL = (1-self.ALPHA) * self.GAMMA * self.prodn(X, s)/L
        return np.append(MPT, MPL)

    def profits(self, X, s, rw):
        """
        profits given factor prices and (T, L, s)
        Args:
            X: vector of factor inputs (X[0] land and X[1] labor)
            s: vector of skill endowments by xtile
            rw: vector of factor prices
        Returns:
            float: vector of marginal products
        """
        return self.prodn(X, s) - np.dot(rw, X) - self.H

    def demands(self, rw, s):
        """
        Competitive factor demands for each skill group in a subeconomy
        Args:
            rw:  vector of factor prices (w[0] land rent and w[1] wage)
            s:  vector of skill endowments by xtile
        Note:
            Farms with negative profits assumed to shut down with zero demands.
        Returns:
            object: 
            vector of factor demands, indicator function if operate production
        """
        a, g = self.ALPHA, self.GAMMA
        r, w = rw
        land = ((w/(g * s * (1 - a))) *
                (((1-a)/a) * (r/w)) **
                (1 - g*(1 - a))) ** (1/(g - 1))

        labor = ((r/(g * s * a)) *
                 ((a/(1-a)) * (w/r)) **
                 (1 - g*a)) ** (1/(g - 1))
        # if fixed cost implies negative profits, zero demands
        X = np.array([land, labor])
        if self.Lucas:
            operate = (self.profits(X, s, rw) >= w)    # For Lucas
        else:
            operate = (self.profits(X, s, rw) >= 0)    # relevant if fixed costs
        return X*operate

    def excessD(self, rw, Xbar, s):
        """
        Total excess land and labor demand given factor prices in
        subeconomy with Xbar supplies
        returns excess demand in each market
        """
        XD = self.demands(rw, s)
        TE, LE = Xbar
        if self.Lucas:   #In Lucas model operators cannot supply labor.
            workers = (self.N - np.count_nonzero(XD[1]>0))*(LE/self.N)
        else:
            workers = LE

        res = np.array([np.sum(XD[0]) - TE,
                        np.sum(XD[1]) - workers])
        return res

    def smallhold_eq(self, Xbar, s):
        """
        Solves for market clearing factor prices in sub-economy with Xbar supplies.

        Solves analytically. Eqn factor prices then off marginal products 
        Args:
            X:  vector of factor inputs (X[0] land and X[1] labor)
            s:  vector of skill endowments in the subeconomy

        Returns:
            res (named tuple): factor prices and demands res.w, res.X
        """
        if self.analytic:     # for specific CobbDouglas
            S = np.sum(s)
            Li = (s/S)*Xbar[1]
            Ti = (s/S)*Xbar[0]
            Xs = np.array([Ti, Li])
            WR = self.marginal_product(Xs[:, -1], s[-1])  #equalized, so any HH will do
        else:  # Numeric solution should work for any demands
            w0 = np.array([0.45, 0.47])  #rw guess

            def f(w):
                return np.sum(self.excessD(w, Xbar, s)**2)

            res = minimize(f, w0, method='Nelder-Mead')
            WR = res.x
            Xs = self.demands(WR, s)
        result = namedtuple('result', ['w', 'X'])
        res = result(w=WR, X=Xs)
        return res

    def smallhold_eq0(self, Xbar, s):
        """
        Solves for market clearing factor prices in economy with Xbar supplies.
        Solve analytically or numerically (minimizes sum of squared excess demands)
        Args:
            X:  vector of factor inputs (X[0] land and X[1] labor)
            s:  vector of skill endowments by xtile
            analytic (bool): by default solve analytically
        Returns:
            res (named tuple): factor prices and demands res.w, res.X
        """

        if self.analytic:     # for specific CobbDouglas
            gamma = self.GAMMA
            s_fringe, s_R = s[0:-1], s[-1]
            psi = np.sum((s_fringe/s_R)**(1/(1-gamma)))
            Lr = Xbar[1]/(1+psi)
            Tr = Xbar[0]/(1+psi)
            L_fringe = Lr*(s_fringe/s_R)**(1/(1-gamma))
            T_fringe = Tr*(s_fringe/s_R)**(1/(1-gamma))
            Xs = np.array([np.append(T_fringe, Tr), np.append(L_fringe, Lr)])
            WR = self.marginal_product(Xs[:, -1], s[-1])
        else:  # Numeric solution should work for any demands
            w0 = np.array([0.2, 0.2])  #rw guess

            def f(w):
                return np.sum(self.excessD(w, Xbar, s)**2)

            res = minimize(f, w0, method='Nelder-Mead')
            WR = res.x
        Xs = self.demands(WR, s)
        result = namedtuple('result', ['w', 'X'])
        res = result(w=WR, X=Xs)
        return res


    def cartel_income(self, Xr, theta):
        """
        Cartel group's income from profits and factor income
        when cartel uses (tr,lr) fringe has (TBAR-tr,LBAR-lr)
        """
        # at present cartel is always last index farm
        Tr, Lr = Xr
        #print(Tr)
        #print(Lr)
        s_fringe, s_R = self.s[0:-1], self.s[-1]  # landlord is last farmer
        wr,_ = self.smallhold_eq([self.TBAR - Tr, self.LBAR - Lr], s_fringe)
        y = self.prodn(Xr, s_R) - \
            np.dot(wr, [Tr-self.TBAR*theta,
                              Lr-self.LAMBDA*self.LBAR])
        #print("cartel:  Tr={0:8.3f}, Lr={1:8.3f}, y={2:8.3f}".format(Xr[0],
        #Xr[1],y))
        return y

    def cartel_eq(self, theta, guess=[40, 20]):
        """
        Cartel chooses own factor use (and by extension how much to
        withold from the fring to max profits plus net factor sales)
        Returns: [w,r], [Ti, Li]
        """
        def f(X):
            # print('X=', X)
            return -self.cartel_income(X, theta)
        res = minimize(f, guess, method='Nelder-Mead')
        XR = res.x
        #print('XR:',XR)
        fringe = self.smallhold_eq([self.TBAR, self.LBAR]-XR, self.s[0:-1])
        XD = np.vstack((fringe.X.T, XR)).T
        WR = fringe.w

        result = namedtuple('result', ['w', 'X'])
        cartel_res = result(w= WR, X= XD)
        return cartel_res

    def print_eq(self, res):
        '''Print out the named tuple returned from equilibrium solution'''
        [w,r], [T,L] = res
        print(f'(w, r) = ({w:0.2f}, {r:0.2f}) ')
        print(f'Ti = {np.array2string(T, precision=2)} ')
        print(f'Li = {np.array2string(L, precision=2)} ')


    def print_params(self):
        """
        Display parameters alphabetically
        """
        params = vars(self).items()
        for itm in params:
            if type(itm[1]) is np.ndarray:
                print()
                if len(itm[1])> 10:
                    print(itm[0], '(-10 tail)=', itm[1][-10:], end=', ')
                else:
                    print(itm[0], '=', itm[1][-6:], end=', ')
                print()
            else:
                print(itm[0], '=', itm[1], end=', ')
                
class EconomyNoLandMarket(Economy):
    """
    This class allocates land exogenously and labor is chosen endogenously.
    
    The landlord receives theta*Tbar and fringe gets (1-theta)*Tbar
    
    For ease of programming, we  will ignore the case where `analytic=False`
    
    """
    
    def average_product(self, X, s):
        
        T, L = X
        APL = s*self.prodn(X, s)/L
        return APL
    
    def smallhold_eq(self, Xbar, s):
        """calculates the smallholder eq for the fringe under no land market

        Args:
            Xbar (np.array): keeping this for compatibility, but it will only have one endogenous variable, labor
            s (np.array): skills of each peasant

        Returns:
            namedtuple : a namedtuple with resulting wages and land/labor chosen
        """
        
        S = np.sum(s)
        Li = (s/S)*Xbar[1]
        Ti = (s/S)*Xbar[0]
        Xs = np.array([Ti, Li])
        WR = self.average_product(Xs[:, -1], s[-1])  #equalized, so any HH will do
        result = namedtuple('result', ['w', 'X'])
        res = result(w=WR, X=Xs)
        
        return res
    
    def cartel_income(self, Xr, theta):
        # at present cartel is always last index farm
        Tr, Lr = Xr
        # print(Tr)
        # print(Lr)
        s_fringe, s_R = self.s[0:-1], self.s[-1]  # landlord is last farmer
        wr,_ = self.smallhold_eq([self.TBAR - Tr, self.LBAR - Lr], s_fringe)
        y = self.prodn(Xr, s_R) - wr*(Lr-self.LAMBDA*self.LBAR)
        #print("cartel:  Tr={0:8.3f}, Lr={1:8.3f}, y={2:8.3f}".format(Xr[0],
        #Xr[1],y))
        return y

    def cartel_eq(self, theta, guess=20):
        """
        Cartel chooses own factor use (and by extension how much to
        withold from the fring to max profits plus net factor sales)
        """
        def f(L):
            # print('X=', X)
            X = [theta*self.TBAR, L]
            return -self.cartel_income(X, theta)
        res = minimize(f, guess, method='Nelder-Mead')
        XR = res.x
        #print('XR:',XR)
        fringe = self.smallhold_eq([(1-theta)*self.TBAR, self.LBAR - XR], self.s[0:-1])
        XD = np.append(fringe.X.T[:,1], XR)
        WR = fringe.w

        result = namedtuple('result', ['w', 'X'])
        cartel_res = result(w= WR, X= XD)
        return cartel_res
    

#%%
class CESEconomy(Economy):

    """
    sub class of Economy class but with two factor CES
    """

    def __init__(self, N):  # constructor to set initial parameters.
        super(CESEconomy, self).__init__(N)  # inherit properties
        # if None supplied use defaults
        self.N         = N # of quantiles (number of skill groups)
        self.RHO       = 0.8    # homogeneity factor
        self.PHI       = 0.5    # alpha (land) for production function
        self.aL        = 1.0    # landlord share of labor
        self.aT        = 1.1    # Total Land Endowment

    def __repr__(self):
        return 'CESEconomy(N={}, GAM={}, TBAR={}, LBAR={})'.format(self.N, self.GAMMA, self.TBAR, self.LBAR)

    def prodn(self, X, s):
        Y = s*(self.PHI*X[0]**(self.RHO) + (1-self.PHI)*X[1]**(self.RHO))  \
            ** (self.GAMMA/self.RHO)
        return Y

    def marginal_product(self, X, s):
        """ Production function technoogy """
        common = s*(self.PHI*X[0]**self.RHO+(1-self.PHI)*X[1]**self.RHO) \
            ** ((1+self.RHO)/self.RHO)
        MPT = common * self.PHI*X[0]**(-self.RHO-1)
        MPL = common * (1-self.PHI)*X[1]**(-self.RHO-1)
        return np.append(MPT, MPL)    
    

#%%
class MirEconomy(Economy):
    """ 
    sub class of Economy class but with Mir rules in subeconomy
    
    """
        
    def demands(self, rw, s):
        """
        factor demands for each skill group in a SUBECONOMY OF THE MIR
        Args:
            rw:  vector of factor prices (w[0] land rent and w[1] wage)
            s:  vector of skill endowments by xtile
        Note:
            Farms with negative profits assumed to shut down with zero demands.
        Returns:
            object: 
            vector of factor demands, indicator function if operate production
        """
        a, g = self.ALPHA, self.GAMMA
        r, w = rw
        
        s_fringe, s_R = s[0:-1], s[-1]
        
        ## Create average skill in mir
        
        s_mir = s_fringe.sum()/((self.N-1))**g
        
        land = ((w/(g * s_mir * (1 - a))) *
                (((1-a)/a) * (r/w)) **
                (1 - g*(1 - a))) ** (1/(g - 1))

        labor = ((r/(g * s_mir * a)) *
                 ((a/(1-a)) * (w/r)) **
                 (1 - g*a)) ** (1/(g - 1))
        
        # if fixed cost implies negative profits, zero demands
        X = np.array([land, labor])
        if self.Lucas:
            operate = (self.profits(X, s_mir, rw) >= w)    # For Lucas
        else:
            operate = (self.profits(X, s_mir, rw) >= 0)    # relevant if fixed costs
        return X*operate
        
    def smallhold_eq(self, Xbar, s):
        """
        Solves for market clearing factor prices in economy with Xbar supplies, assuming 
        a Mir of N-1 agents that distribute land and labor by some 
        Solve analytically or numerically (minimizes sum of squared excess demands)
        Args:
            X:  vector of factor inputs (X[0] land and X[1] labor)
            s:  vector of skill endowments by xtile
            analytic (bool): by default solve analytically
        Returns:
            res (named tuple): factor prices and demands res.w, res.X
        """

        if self.analytic:     # for specific Cobb-Douglas
            gamma = self.GAMMA
            s_fringe, s_R = s[0:-1], s[-1]
        
            ## Create average skill in mir
        
            s_mir = s_fringe.sum()/((self.N-1))**gamma
            
            psi = np.sum((s_mir/s_R)**(1/(1-gamma)))
            Lr = Xbar[1]/(1+psi)
            Tr = Xbar[0]/(1+psi)
            L_fringe = Lr*(s_mir/s_R)**(1/(1-gamma))
            T_fringe = Tr*(s_mir/s_R)**(1/(1-gamma))
            Xs = np.array([np.append(T_fringe, Tr), np.append(L_fringe, Lr)])
            WR = self.marginal_product(Xs[:, -1], s[-1])
        else:  # Numeric solution should work for any demands
            w0 = np.array([0.2, 0.2])  #rw guess

            def f(w):
                return np.sum(self.excessD(w, Xbar, s)**2)

            res = minimize(f, w0, method='Nelder-Mead')
            WR = res.x
        Xs = self.demands(WR, s)
        result = namedtuple('result', ['w', 'X'])
        res = result(w=WR, X=Xs)
        return res


# End of class definitions

def scene_print(E, numS=5, prnt=True, detail=True,
                mir = False):
        """
        Creates numS land ownership scenarios by varying land gini THETA
        calculating competitive and market-power distorted equilibria for each
        Prints results if flags are on.
        Args:
          E -- Instance of an Economy object
          mir -- Whether to find a cartel equilibrium with a Mir subeconomy
          numS -- number of values of theta
          prnt -- print table if True
        Returns:
          [Xc,Xr,wc,wr]  where
            Xc -- Efficient/Competitive landlord factor use
            Xc -- Efficient/Competitive landlord factor use
            Xr -- numS x 2 matrix, Xr[theta] = Landlords' distorted use
            wc -- competitive factor prices
            wr -- wr[theta] distorted competitive factor prices
        """
        
        if mir:
            E_distort = MirEconomy(E.N)
            
            for attr, value in E.__dict__.items():
                setattr(E_distort, attr, value)
        else:
            E_distort = E
                    
                
        # competitive eqn when landlord is another price taker 
        comp = E.smallhold_eq([E.TBAR, E.LBAR], E.s)
        (rc,wc), Xc = comp.w, comp.X
        Xrc = Xc[:,-1]   # landlord's factor use
        #
        guess = Xrc
        # distorted equilibria at different land ownership theta
        theta = np.linspace(0,1,numS+1)
        theta[-1] = 0.97
        if prnt:
            print("\nAssumed Parameters")
            print("==================")
            E.print_params()
            print()

            print(("\nTheta  [  Tr,  Lr  ] [   rM,  wM  ]  w/r  "), end=' ')
            if detail:
                print('|  F() [T_hire] [T_sale] [L_hire]')
            else:
                print()
            print(("="*78))

                
            print(("  eff  [{0:5.1f},{1:5.1f}]".format(Xrc[0],Xrc[1])), end=' ')
            print(("[{0:4.3f}, {1:4.3f}]".format(rc, wc)), end=' ')
            print((" {0:4.2f} ".format(wc/rc)), end=' ')
            if detail:
                    print(("| {0:5.2f} ".format(E.prodn(Xrc, E.s[-1]))), end=' ')
                    print((" {0:5.2f} ".format(Xrc[0]*rc)), end=' ')
                    print((" {0:6.2f} ".format(Xrc[1]*wc)))
            else:
                print()

    
        Xr = np.zeros(shape=(numS+1, 2))  # Xr - load factor use for each theta
        Tr, Lr = np.zeros(numS + 1), np.zeros(numS + 1)  # Xr - load factor use for each theta
        rw = np.zeros(shape=(numS+1,2))
        w, r = np.zeros(numS + 1), np.zeros(numS + 1)


        for i in range(numS+1):
            cartelEQ = E_distort.cartel_eq(theta[i], guess)
            Xr[i] = cartelEQ.X[:, -1]
            Tr[i], Lr[i] = Xr[i]
            rw[i] = cartelEQ.w
            r[i], w[i] = rw[i]
            guess = Xr[i]
            if prnt:
                print((" {0:3.2f}".format(theta[i])), end=' ')
                print((" [{0:5.1f},{1:5.1f}]".format(Tr[i],Lr[i])), end=' ')
                print(("[{0:5.3g}, {1:5.3f}] {2:5.2f}" \
                .format(r[i],w[i],w[i]/r[i])), end=' ')
                if detail:
                    print((" | {0:5.2f} ".format(E_distort.prodn(Xr[i], E.s[-1]))), end=' ')
                    print((" {0:6.2f} ".format(Xr[i,0]*rw[i,0])), end=' ')
                    print((" {0:6.2f} ".format(theta[i] * E_distort.TBAR * rw[i, 0])), end=' ')
                    print((" {0:6.2f} ".format(Xr[i,1]*rw[i,1])), end=' ')
                print("")
        if prnt:
            print(("="*78))

        return (Xrc, Xr, [rc,wc], rw)


def factor_plot(ECO, Xrc, Xr, fig = None, ax=None):
    
    ## Create figure and axis object
    
    if ax is None:
        fig, ax = plt.subplots(figsize=(8,7))
        
    numS = len(Xr)-1
    theta = np.linspace(0, 1, numS+1)
    Tr, Lr = Xr[:, 0], Xr[:, 1]
    Tr_net = Tr-np.array(theta) * ECO.TBAR
    Lr_net = Lr - ECO.LAMBDA * ECO.LBAR
    # print(Tr_net, Lr_net)
    Trc_net = Xrc[0]*np.ones(numS+1)-np.array(theta)*ECO.TBAR
    Lrc_net = Xrc[1]*np.ones(numS+1)-ECO.LAMBDA*ECO.LBAR
    ax.set_title(f"Landlord net factor hire for $\gamma$ ={ECO.GAMMA}" )
    ax.plot(theta, Tr_net, '-ro', label='distorted land')
    ax.plot(theta, Trc_net, label='efficient land')
    ax.plot(theta, Lr_net, '-b*', label='distorted labor')
    ax.plot(theta, Lrc_net, label='efficient labor')
    ax.grid(axis='x')
    ax.axhline(y=0, linestyle='dashed')
    ax.set_ylim(-100, ECO.TBAR) 
    # plt.xlabel(r'$\gamma =$')
    ax.legend(loc='lower left',title='net hiring of')
    return ax

def TLratio_plot(ECO, Xrc, Xr, fig = None, ax = None):
    if ax is None:
        fig, ax = plt.subplots(figsize = (7,5))
    numS = len(Xr)-1
    theta = np.linspace(0, 1, numS+1)
    ax.plot(theta, Xr.T[0][:]/Xr.T[1][:], '-ro', label='distorted')
    ax.plot(theta, (Xrc[0]/Xrc[1])*np.ones(numS+1), '--', label='efficient')
    ax.legend(loc='upper left',title='Land/Labor ratio')
    ax.set_title(f"Land to labor ratio on landlord farm for $\gamma$ ={ECO.GAMMA}" )
    ax.grid(axis='x')
    return ax

#%%
if __name__ == "__main__":
    """Sample use of the Economy class """

    s = np.array([1.,  1.,  1.,  1.,  1.])
    N = len(s)
    E = Economy(N)    # an instance takes N length as parameter
    E.ALPHA = 0.5
    E.GAMMA = 0.90

    E.smallhold_eq([E.TBAR, E.LBAR], s)

    (Xrc, Xr, wc, wr) = scene_print(E, 10, detail=True)

    factor_plot(E,Xrc,Xr)
    TLratio_plot(E,Xrc,Xr)