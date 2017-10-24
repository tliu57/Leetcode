class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.allServers = []
        self.serverDict = {}

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        # write your code here
        idx = len(self.allServers)
        self.allServers.append(server_id)
        self.serverDict[server_id] = idx 

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        # write your code here
        last_server_idx = len(self.allServers) - 1
        remove_server_idx = self.serverDict[server_id]
	last_server_id = self.allServers[last_server_idx]
        self.allServers[remove_server_idx] = last_server_id
	self.serverDict[last_server_id] = remove_server_idx
        self.serverDict.pop(server_id)
        del self.allServers[-1] 

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        # write your code here
        import random
        return random.choice(self.allServers)



sol = LoadBalancer()
sol.add(1)
sol.add(2)
sol.add(3)
sol.add(4)
sol.add(5)
sol.add(6)
sol.remove(1)
sol.remove(6)
print sol.pick()
print sol.pick()
sol.add(11)
sol.add(22)
sol.add(33)
