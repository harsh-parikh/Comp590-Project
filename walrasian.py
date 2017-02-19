# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 16:55:48 2017

@author: Harsh
"""

import numpy as np
import scipy

def cobbDouglas(exponent):
    def utilityFn(point):
        shp = np.shape(exponent)
        u = 1
        for i in range(0,shp[1]):
            u = u*np.power(point[0,i],exponent[0,i])
        return u
    return utilityFn

def gradient(f,point,eps):
    #find gradient of function f at a given point
    #point is a row vector
    shp = np.shape(point)
    ident = np.identity(shp[1])
    dx = ident*eps
    x1 = np.ones([shp[1],shp[0]])*point
    x2 = x1 + dx
    df = np.zeros([shp[0],shp[1]])
    for i in range(shp[1]):
        df[0,i] = ( f( np.array([x2[i,:]]) ) - f( np.array([x1[i,:] ]))) / ( dx[i,i] )
    return df
    
def solution(coeffArray,totalEndownments,quantum):
    #find solution for coefficient*x = 0
    # s.t. X_i >= x_i >= 0 and sum(x_i)>0
    #shape of coeffArray[1,length]
    c = coeffArray[0]
    #setting up A
    A_1 = np.identity( len ( totalEndownments[0] ) )
    A_2 = -1*A_1
    aLast = -1 * np.ones ([ 1, len(totalEndownments[0]) ] )
    A = np.vstack((A_1,A_2))
    A = np.vstack((A,aLast))
    A = np.vstack((A,-1*coeffArray))
    #setting up b
    b = totalEndownments[0] 
    b = np.concatenate( ( b,[0 for i in range( 0, len( totalEndownments[0] ) ) ],[-1*quantum],[0] ) )    
    #calling linear program to optimize
    from scipy.optimize import linprog
    res = linprog(c, A_ub=A, b_ub=b, options={"disp": False})
    return res['x']

def walrasianEq(endownments,utilityFunctions,quantum):
    u1, u2 = utilityFunctions
    e1, e2 = endownments
    v1 = u1(e1)
    v2 = u2(e2)
    p1 = gradient(u1,e1,np.finfo(float).eps)
    p2 = gradient(u2,e2,np.finfo(float).eps)
    p = p1-p2
    while((p.any()==0)!=True):
        x = solution(p,(e1+e2),quantum)
        transaction = np.sign(p)*x
        e1 = e1 + transaction #there is mistake in sign here, we need to get sign from p vector
        e2 = e2 - transaction
        p1 = gradient(u1,e1,np.finfo(float).eps)
        p2 = gradient(u2,e2,np.finfo(float).eps)
        p = p1-p2
    return (e1,e2,p1,p2)
    