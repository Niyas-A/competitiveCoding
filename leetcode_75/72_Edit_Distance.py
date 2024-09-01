class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1, len2 = len(word1)+1, len(word2)+1
        dpt= [[0]*len2 for i in range(len1) ] #len1 as row, len2 as col
        for i in range(len2):  # here len2=4, but i will be from 0 to 3
            dpt[0][i]=i
        
        for i in range(len1):
            dpt[i][0]=i
        
        for i in range (1, len1):
            c = word1[i-1]
            for j in range(1, len2):
                insert = dpt[i-1][j]
                replace = dpt[i-1][j-1]
                delete = dpt[i][j-1]
                if(word2[j-1]==c):
                    dpt[i][j]= replace
                else:
                    dpt[i][j]= min(insert, replace, delete)+1
        
        return dpt[len1-1][len2-1]
