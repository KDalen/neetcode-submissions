class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l<r:
            while not (s[l].isalpha() or s[l].isnumeric()) and l<r:
                l+=1
            while not (s[r].isalpha() or s[r].isnumeric()) and l<r:
                r-=1  

            if s[l].lower() != s[r].lower():
                print(s[l],s[r])
                return False
            l +=1
            r-=1
        return True