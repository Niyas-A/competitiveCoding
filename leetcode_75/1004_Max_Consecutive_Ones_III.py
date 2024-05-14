class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = 0
        count = 0
        max_count = 0
        shift = 0
        while right < n:
            if nums[right] == 1:
                right += 1
                count += 1      
            else:
                if shift < k:
                    right += 1
                    count += 1
                    shift += 1 
                else:
                    if nums[left] == 0:
                        shift -= 1
                    left += 1
                    count -= 1
            if count > max_count:
                max_count = count
        return max_count