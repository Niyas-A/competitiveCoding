class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mat = [[0 for _ in range(n)] for _ in range(m)]
        # print(mat)
        for i in range(m):
            for j in range(n):
                if i-1<0 and j-1<0:
                    mat[i][j] = 1
                elif i-1<0:
                    mat[i][j] = mat[i][j-1]
                elif j-1<0:
                    mat[i][j] = mat[i-1][j]
                else:
                    mat[i][j] = mat[i-1][j] + mat[i][j-1]
        return mat[m-1][n-1]
                    