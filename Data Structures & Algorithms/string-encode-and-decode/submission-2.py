class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res+=word+"√"
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        word = ''
        while i < len(s):
            if s[i] == '√':
                print('word')
                print(word)
                res.append(word)
                word = ''
            else:
                word+=s[i]

            i+=1
        print(res)
        return res
