import numpy as np

class Agent:
    def __init__(self, index, goods, util):
        self.index = index
        self.goods = goods
        self.util  = util

    def getUtility(self):
        return self.util(self.goods.quantity)

    def setAdj(self, adj):
        #sellTo is a list with True values for which agents it can sell to
        self.sellTo = adj[self.index,:]
        #buyFrom is a list with True values for which agents it can buy from
        self.buyFrom = adj[:, self.index]
