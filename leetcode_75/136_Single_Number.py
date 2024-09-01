class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        n = len(nums)
        if n == 1:
            return nums[0]
        for i in range(n):
            x^=nums[i]
            # print(x,nums[i])
        return x
        