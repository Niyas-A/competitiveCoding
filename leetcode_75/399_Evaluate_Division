class Solution(object):
    def dfs(self, x, y, graph, vis, ans, temp):
        if x in vis:
            return
        vis.add(x)
        if x == y:
            ans[0] = temp
            return
        for z, val in graph[x].items():
            self.dfs(z, y, graph, vis, ans, temp * val)

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = {}
        # nodes = set()
        for i in range(len(equations)):
            x, y = equations[i]
            value = values[i]
            if x not in graph:
                graph[x] = {}
            if y not in graph:
                graph[y] = {}
            graph[x][y] = value
            graph[y][x] = 1.0 / value
            # nodes.add(x)
            # nodes.add(y)
        # print(nodes)
        print(graph)

        result = []
        # check query
        for query in queries:
            x, y = query
            if x not in graph or y not in graph:
                result.append(-1.0)
            else:
                vis = set()
                ans = [-1.0]
                temp = 1.0
                self.dfs(x, y, graph, vis, ans, temp)
                result.append(ans[0])
        return result
        