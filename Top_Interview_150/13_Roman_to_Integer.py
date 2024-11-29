class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnv = {'I': 1,'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = len(s)
        res = 0
        for i,char in enumerate(s):
            if i<n-1 and cnv[s[i]]>=cnv[s[i+1]]:
                res += cnv[s[i]]
            elif i<n-1:
                res -= cnv[s[i]]
            else:
                res += cnv[s[i]]
        return res