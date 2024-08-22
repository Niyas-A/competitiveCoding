class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def backtrack(start, target, k):
            if k == 0 and target == 0:
                return [[]]
            if k == 0 or target < 0:
                return []
            ans = []
            for i in range(start, 10):
                for combo in backtrack(i+1, target-i, k-1):
                    ans.append([i] + combo)
            return ans
        
        return backtrack(1, n, k)

        