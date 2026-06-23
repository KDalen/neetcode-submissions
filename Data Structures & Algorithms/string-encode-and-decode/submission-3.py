from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            # Store the length + delimiter + the word itself
            res += str(len(word)) + "/" + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Find the next delimiter to isolate the length integer
            while s[j] != '/':
                j += 1
            
            # Extract the length of the upcoming word
            length = int(s[i:j])
            
            # Extract the actual word using the length
            word_start = j + 1
            word_end = word_start + length
            res.append(s[word_start:word_end])
            
            # Move the pointer to the start of the next length integer
            i = word_end
            
        return res