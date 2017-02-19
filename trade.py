# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 21:45:04 2017

@author: Harsh
"""
import numpy as np
import walrasian
import findEquilibrium

def trade(network,quantum,itr):
    #randomly choose an agent, then randomly choose a trading partner
    agents = network.agents
    n = len(agents)
    adj = network.adj
    for i in range(itr):
        ai = np.random.randint(0,n)
        bi = np.random.randint(0,n)
        while(adj[ai,bi]!=1 or ai==bi):
            bi = np.random.randint(0,n)
        (agents[ai], agents[bi]) = findEquilibrium.findEquilibrium(agents[ai], agents[bi],adj,quantum)
        print (network.getUtilities())
    return network