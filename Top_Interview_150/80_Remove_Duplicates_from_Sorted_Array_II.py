class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        k = 1
        n = len(nums)
        prev = nums[i]
        i += 1
        while i<n:
            if prev == nums[i]:
                while i<n and nums[i]==prev:
                    i += 1
                if i-1<n:
                    nums[k]=nums[i-1]
                    k += 1
            else:
                nums[k]=nums[i]
                k += 1
                i += 1
            prev = nums[i-1]
        return k