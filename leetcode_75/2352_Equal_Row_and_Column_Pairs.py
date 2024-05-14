class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # print(set(grid))
        n = len(grid)
        # hsum = [0]*n
        # vsum = [0]*n
        # print(hsum)
        h = ['']*n
        v = ['']*n
        # print(h)
        for i,vec in enumerate(grid):
            for j,e in enumerate(vec):
                h[i] += str(e) + '-'
                v[j] += str(e) + '-'
            # print(vec)
            # h[i] += str(vec)
            # [h[i] += str(v) for v in vec]
        # print(h)   
        # print(v)   
        h1 = Counter(h)
        v1 = Counter(v)
        count = 0
        # print(h1)
        # print(v1)
        for key in h1.keys():
            if key in v1.keys():
                count += v1[key]*h1[key]
        # print(count)
        #     hsum[i] = sum(vec)
        #     for j in range(n):
        #         vsum[j] += vec[j]
        # print(hsum)
        # print(vsum)
        # print(Counter(hsum))
        # print(Counter(vsum))
        
        return count
        