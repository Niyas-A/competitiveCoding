class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 1:
            return True
        jumb = 0
        for i in range(0,n-1):
            jumb = max(jumb-1,nums[i])
            if jumb<1:
                return False
        return True
        