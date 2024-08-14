class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        rows = len(maze)
        cols = len(maze[0])
        start_row, start_col = entrance
        maze[start_row][start_col] = '+'
        q = deque([(start_row,start_col,0)])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        while q:
            curr_row, curr_col, curr_dist = q.popleft()
            for d in directions:
                next_row = curr_row + d[0]
                next_col = curr_col + d[1]

                if 0<= next_row <rows and 0<= next_col <cols and maze[next_row][next_col]=='.':
                    if 0 == next_row or next_row == rows-1 or next_col == 0 or next_col == cols-1:
                        return curr_dist + 1
                    q.append((next_row, next_col, curr_dist+1))
                    maze[next_row][next_col]='+'
        return -1     