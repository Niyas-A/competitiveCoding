class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]*(n+1)
        if n == 0:
            return [0]
        res[1] = 1
        if n == 1:
            return [0,1]
        div = 1
        for i in range(2,n+1):
            if i%div == 0:
                div *= 2
            res[i] = 1 + res[i%div]
        return res

        