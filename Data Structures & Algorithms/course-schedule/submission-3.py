class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for cur, pre in prerequisites:
            graph[cur].append(pre)
        completed = set()
        def dfs(cur, path):
            if cur in completed:
                return True
            if cur in path:
                return False

            path.add(cur)
            for nei in graph[cur]:
                if not dfs(nei, path):
                    return False

            path.remove(cur)
            completed.add(cur)
            return True

        for val in range(numCourses):
            if not dfs(val, set()):
                return False
        return True


