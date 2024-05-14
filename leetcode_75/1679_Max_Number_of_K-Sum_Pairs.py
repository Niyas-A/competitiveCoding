class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sNum = sorted(nums)
        # print(sNum)
        left = 0
        right = len(sNum)-1
        count = 0
        while right>left:
            if sNum[right]+sNum[left]==k:
                count += 1
                right -=  1
                left += 1 
                continue
            if sNum[right]+sNum[left]>k:
                right -= 1
            else :
                left += 1
        return count