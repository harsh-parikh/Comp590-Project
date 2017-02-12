import numpy as np

class Agent:
    def __init__(self, index, goods, util):
        self.index = index
        self.goods = goods
        self.util  = util

    def getUtility(self):
        result = 1
        for good, i in enumerate(goods):
            result *= good.quantity**util[i]
        return result

    def setAdj(self, adj):
        #sellTo is a list with True values for which agents it can sell to
        self.sellTo = adj[self.index,] == 1.toList()

        #buyFrom is a list with True values for which agents it can buy from
        self.buyFrom = adj[, self.index] == 1.toList()
