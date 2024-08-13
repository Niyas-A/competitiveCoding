class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        edges = set()

        for x,y in connections:
            graph[x].append(y)            
            graph[y].append(x)            
            edges.add((x,y))
        
        changes = 0
        seen = {0}

        def dfs(node):
            changes = 0
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    if (node,neighbor) in edges:
                        # print(node,neighbor)
                        changes += 1
                    changes += dfs(neighbor)
            return changes
        
        return dfs(0)