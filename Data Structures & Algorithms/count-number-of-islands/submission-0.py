class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #strategy dfs 
        islands = 0
        seen = [[0] * len(grid[0]) for _ in range(len(grid))]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if int(grid[r][c]) == 1 and seen[r][c] == 0:
                    islands+=1
                    #DFS
                    stack = [(r,c)]
                    while stack:
                        row, col = stack.pop()
                        if row < len(grid) and col < len(grid[0]) and row >=0 and col>=0 and int(grid[row][col]) == 1 and not seen[row][col]:
                            seen[row][col] = 1
                            stack.append((row + 1,col))
                            stack.append((row - 1, col))
                            stack.append((row, col + 1))
                            stack.append((row, col - 1))
        return islands
                        

