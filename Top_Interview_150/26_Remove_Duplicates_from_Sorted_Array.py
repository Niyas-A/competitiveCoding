class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        numset = set()
        for num in nums:
            if num not in numset:
                nums[k]=num
                numset.add(num)
                k+=1
        # print(k)
        return k