class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        kMod = int(1e9) + 7
        
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 5
        
        dp_i_minus_3 = 1  
        dp_i_minus_2 = 2 
        dp_i_minus_1 = 5  

        for _ in range(4, n + 1):
            dp_i = (2 * dp_i_minus_1 + dp_i_minus_3) % kMod

            dp_i_minus_3, dp_i_minus_2, dp_i_minus_1 = dp_i_minus_2, dp_i_minus_1, dp_i

        return dp_i_minus_1
