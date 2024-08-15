from collections import deque 
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    q.append((i,j,0))
        max_dist = 0
        while q:
            curr_row, curr_col, curr_dist = q.popleft()
            for d in directions:
                next_row = curr_row + d[0]
                next_col = curr_col + d[1]

                if 0<= next_row <rows and 0<= next_col <cols and grid[next_row][next_col]==1:
                    q.append((next_row, next_col, curr_dist+1))
                    grid[next_row][next_col]=2
                    if max_dist < curr_dist + 1:
                        max_dist = curr_dist + 1
        # check any orrange left
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    return -1
        return max_dist