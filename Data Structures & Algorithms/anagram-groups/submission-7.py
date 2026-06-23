class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)

        for i in range(len(strs)):
            chars = [0]*26
            for j in range(len(strs[i])):
                chars[ord(strs[i][j]) - ord('a')] += 1

            mapping[tuple(chars)].append(strs[i])
        
        return list(mapping.values())