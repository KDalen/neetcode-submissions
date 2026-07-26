
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res= [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack:
                if temperatures[i] > temperatures[stack[-1]]:
                    val = stack.pop()
                    res[val] = i-val
                else:
                    break
            stack.append(i)

        return res

            