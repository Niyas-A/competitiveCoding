class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        # if target > sum(nums) or target < nums[0]:
        #     return 0
        # left, right = 0, 1
        # if nums[0] >= target:
        #     return 1
        # n = len(nums)
        # cur_sum = sum(nums[left]+nums[right])
        # while right<n and cur_sum < target:
        #     right += 1
        #     cur_sum += nums[right]
        # lst = []
        # while right<n:
        #     if cur_sum >= target:
        #         lst.append(right - left)
        #         left += 1
        #         if left<
        #         cur_sum -= nums[left]
        #     else:
        #         right += 1
        #         if right < n:
        #             cur_sum += nums[right]
        #     elif cur_sum > target:
        #         left += 1
        #         if left < right:
        #             cur_sum -= nums[left-1]
        l, total = 0, 0
        res = float('inf')

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r-l+1,res)
                total -= nums[l]
                l += 1
        return 0 if res == float('inf') else res


        