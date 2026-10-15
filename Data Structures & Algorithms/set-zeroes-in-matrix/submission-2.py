class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col = False
        n = len(matrix[0])
        m = len(matrix)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if j == 0:
                        col = True
                    else:
                        matrix[i][0] = 0
                        matrix[0][j] = 0

        # bool for first col use 0,0 for first row
        for i in range(m-1,0,-1):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(n-1,0,-1):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        if col:
            for i in range(m):
                matrix[i][0] = 0
            
            


