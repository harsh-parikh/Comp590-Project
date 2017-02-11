class Agent:
    def __init__(self, index, endowments, util):
        self.index = index
        self.endowments = endowments
        self.util = util

    def setAdj(adj):
        #sellTo is a list with True values for which agents it can sell to
        self.sellTo = adj[self.index,] == 1.toList()

        #buyFrom is a list with True values for which agents it can buy from
        self.buyFrom = adj[, self.index] == 1.toList()
