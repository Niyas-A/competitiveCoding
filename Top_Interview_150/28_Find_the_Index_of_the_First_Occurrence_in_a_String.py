class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        for i in range(n):
            j = 0
            if haystack[i] == needle[j]:
                while i+j < n and j < m and haystack[i+j] == needle[j]:
                    j += 1
                if j == m:
                    return i
        return -1 