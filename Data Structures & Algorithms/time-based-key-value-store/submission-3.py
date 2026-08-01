from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.table = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.table:
            self.table[key].append((value, timestamp))
        else:
            self.table[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        l,r = 0,len(self.table[key])-1
        res=""
        while l<=r:
            mid = (l+r) // 2
            if timestamp >= self.table[key][mid][1]:
                res = self.table[key][mid][0]
                l = mid+1
            else:
                r = mid -1
        return res
        
