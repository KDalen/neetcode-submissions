class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 ==1:
            return False
        for char in s:
            if char in "{[(":
                stack.append(char)
            else:
                if not stack:
                    return False
                val = stack.pop()
                if ((char == "}" and val != "{")
                    or (char == "]" and val != "[")
                    or (char == ")" and val != "(")):
                    return False

        return len(stack) == 0

                    