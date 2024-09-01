class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)
        dp=[[0]*(n+1)for i in range (m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[m][n]
        # if m<=n: 
        #     shortest = text1
        #     longest = text2
        # else:
        #     shortest = text2 
        #     longest = text1
        # count = 0
        # lst = -1
        # for s in shortest:
        #     for j,l in enumerate(longest):
        #         print(j,l)
        #         if s == l and lst<j:
        #             lst = j
        #             count += 1 
        #             break
        # return count
