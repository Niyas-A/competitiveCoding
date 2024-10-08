class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        net_gas = [g-c for g,c in zip(gas,cost)]
        if sum(net_gas) < 0:
            return -1 
        
        tank = 0
        start = 0
        for i,g in enumerate(net_gas):
            tank += g
            if tank<0:
                tank = 0
                start = i+1
        return start