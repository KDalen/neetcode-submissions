class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        l = 0
        charf = {}
        targetf = {}

        for val in s1:
            targetf[val] = 1 + targetf.get(val, 0)

        for r in range(len(s2)):            
            char = s2[r]
            charf[char] = 1+ charf.get(char, 0)

            if r-l+1 > len(s1) :
                charf[s2[l]] = charf.get(s2[l]) -1
                if charf[s2[l]] == 0:
                    charf.pop(s2[l])
                l+=1
            if charf == targetf:
                return True
        return False

