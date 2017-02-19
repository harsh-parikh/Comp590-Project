class Network:
    def __init__(self, agents, adj):
        self.agents = agents
        self.adj = adj

    def getNetwork(self):
        return (self.agents,self.adj)
    
    def getUtilities(self):
        u = [self.agents[i].getUtility() for i in range(0,len(self.agents))]
        return u
