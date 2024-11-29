class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = 0
        r = 0
        while(i<n):
            if s[n-i-1]==' ':
                i += 1
                r += 1
            else:
                break
        while(i<n):
            if s[n-i-1]==' ':
                return i - r
            i += 1
        return n - r
        