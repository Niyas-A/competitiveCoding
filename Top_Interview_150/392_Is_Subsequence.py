class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(s)
        m = len(t)
        i, j = 0, 0
        while i < m and j < n:
            if t[i] == s[j]:
                j += 1
            i += 1

        if j == n:
            return True
        else:
            return False
