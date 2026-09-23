class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # No cycles, fully connected (all reachable)
        # n nodes have n-1 edges done
        if len(edges) != n-1:
            return False
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        completed = set()
        def dfs(cur,prev, path):
            if cur in path:
                return False
            path.add(cur)
            for nei in graph[cur]:
                if nei != prev and not dfs(nei,cur, path):
                    return False
            path.remove(cur)
            completed.add(cur)
            return True

        return dfs(0, 0, set()) and len(completed) == n


