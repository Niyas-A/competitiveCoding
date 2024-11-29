class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        trap_l = []
        trap_r = []
        lowest = 0
        n = len(height)
        for h in height:
            if h>lowest:
                lowest = h
                trap_l.append(0)
            else:
                trap_l.append(lowest - h)
        lowest = 0
        for i in range(n):
            if height[n-i-1]>lowest:
                lowest = height[n-i-1]
                trap_r.append(0)
            else:
                trap_r.append(lowest - height[n-i-1])
        trap = 0
        for i in range(n):
            trap += min(trap_l[i],trap_r[n-i-1])
        return trap