class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # max_sum = 0
        # rob = {}
        # for i in range(len(nums)):
        #     if i not in rob.keys():
        #         # print(i)
        #         rob[i] = nums[i]
        #     for k,v in rob.items():
        #         # print(k,v)
        #         if i-1 not in [k] and i+1 not in [k]:
        #             print(k)
        #             rob[tuple([k] + [i])] = nums[i]+v
        # print(rob)
        # return(max(rob))
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]