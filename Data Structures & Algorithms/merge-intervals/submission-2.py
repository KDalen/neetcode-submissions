class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        res = []
        curr_interval = intervals[0]
        for i in range(1, len(intervals)):
            #merge the intervals
            
            if curr_interval[1] >= intervals[i][0]:
                print("enter", curr_interval)
                curr_interval = [min(curr_interval[0], intervals[i][0]), max(curr_interval[1], intervals[i][1])]
            else:
                res.append(curr_interval)
                curr_interval = intervals[i]
        res.append(curr_interval)
        return res
