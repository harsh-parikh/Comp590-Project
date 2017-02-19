# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 21:25:42 2017

@author: Harsh
"""
import numpy as np
import scipy
import walrasian

def findEquilibrium(A,B,adj,quantum):
    assert adj[A.index, B.index] == 1 
    (eA, eB) = (A.goods.quantity, B.goods.quantity)
    (uA, uB) = (A.util, B.util)
    (xA, xB, pA, pB) = walrasian.walrasianEq((eA, eB),(uA, uB),quantum)
    A.goods.quantity = xA
    A.goods.price = pA
    B.goods.quantity = xB
    B.goods.price = pB
    return (A,B)
    
    
    
    