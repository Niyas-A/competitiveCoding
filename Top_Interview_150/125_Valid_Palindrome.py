class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # n = len(s)
        # left = 0
        # right = n - 1
        # while left < right:
        #     while left < n and not (s[left].isalpha()):
        #         left += 1
        #     while right >= 0 and not (s[right].isalpha()):
        #         right -= 1  
        #     if left == n and right >= 0:
        #         return False
        #     if right == -1 and left < n:
        #         return False 
        #     if left < n and right >= 0 and s[left].lower()!=s[right].lower():
        #         print(left,right,s[left],s[right])
        #         return False
        #     left += 1
        #     right -= 1
        # return True

        c = ''.join([char.lower() for char in s if char.isalnum()])

        return c == c[::-1]