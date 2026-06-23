class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            if target == matrix[i][-1]:
                return True
            elif target < matrix[i][-1]:
                #binary search target
                l,r = 0, len(matrix[i])-1
                while l<=r:
                  
                    mid = l +((r-l) //2)
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        l = mid + 1
                    else:
                        r = mid -1
                return False
            else:
                continue
        return False