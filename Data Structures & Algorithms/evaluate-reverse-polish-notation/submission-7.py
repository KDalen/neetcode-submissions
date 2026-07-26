class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens or tokens[0] in "+-/*":
            return 0
        stack = []
        while tokens:
            val = tokens.pop(0)
            if val in ["+", "-", "*","/"] :
                
                r,l = int(stack.pop()), int(stack.pop())
                print("l,r", l,r)
                print(val)
                if val == "+":
                    stack.append(l+r)
                elif val == "-":
                    stack.append(l-r)
                elif val == "*":
                    stack.append(l*r)
                else:
                    stack.append(l/r)
            else:
                stack.append(val)
        return int(stack.pop())
