# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 23:57:16 2017

@author: Harsh
"""

import agent
import goods
import network
import walrasian
import findEquilibrium
import trade
import numpy as np

def market(numberOfAgents,numberOfGoods,utilityExponents,endownments,adj,quantum):
    m = numberOfAgents
    n = numberOfGoods
    agents = []
    for i in range(0,m):
        u = walrasian.cobbDouglas( np.array( [ utilityExponents[i,:] ] ) )
        g = goods.Goods( np.array( [ endownments[i,:] ] ), np.zeros( (1,n) ) )
        a = agent.Agent(i,g,u)
        a.setAdj(adj)
        agents.append(a)
    net = network.Network(agents,adj)
    netAfterTrade = trade.trade(net,quantum,100)
    return netAfterTrade

m = 3
n = 3
ue = np.array( [ [ 2.0, 1.0, 3.0 ], [ 1.0, 2.0, 1.0 ], [ 1.0, 2.0, 2.0 ] ] )
endw = np.array( [ [ 1, 2, 1 ] , [ 2, 1, 1 ], [ 3, 2, 1 ] ] )
adj = np.array( [ [ 1, 1, 1 ], [ 1, 1, 1 ], [ 1, 1, 1 ] ] )
quantum = 0.05
n1 = market(m,n,ue,endw,adj,quantum)
    