class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        prefixStr = ""
        n = len(strs[0])
        for i in range(n):
            if(strs[0][i] == strs[-1][i]):
                prefixStr += strs[0][i]
            else:
                break
        return prefixStr

