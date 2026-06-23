class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtracking(index, path):
            if index >= len(nums):
                results.append(path[:]) #append copy
                return
            path.append(nums[index])
            backtracking(index+1,path)
            path.pop()

            backtracking(index+1,path)

        backtracking(0,[])
        return results