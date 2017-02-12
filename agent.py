import numpy as np

class Agent:
    def __init__(self, index, goods, util):
        self.index = index
        self.goods = goods
        self.util  = util

    def setAdj(self, adj):
        #sellTo is a single row matrix, True indicates
        #who this agent can sell to
        self.sellTo = adj[self.index,] == 1

        #buyFrom is a single row matrix, False indicates
        #who this agent can buy from
        self.buyFrom = adj[, self.index] == 1

    def getUtility(self):
        result = 1
        for good, i in enumerate(goods):
            result *= good.quantity**util[i]
        return result
