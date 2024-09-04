class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        if n==1:
            return nums[0]
        count = 0
        i = 0
        while i<n-1:
            count = 0
            while nums[i]==nums[i+1] and i<n-1:
                i += 1
                count += 1
                if count >= n//2:
                    return nums[i]
            i += 1
        return 0