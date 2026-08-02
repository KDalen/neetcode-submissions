class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        hash_set = {}
        l = 0
        for r in range(len(s)):
            char = s[r]

            if char in hash_set and hash_set[char] >= l:
                l = hash_set[char] +1

            hash_set[char] = r
            longest = max(longest, r - l +1)

        return longest