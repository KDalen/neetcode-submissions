class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for tok in tokens:
            print(tok)
            if tok == '+':
                a = stack.pop()
                b = stack.pop()
                print(a,b,tok)
                stack.append(int(a)+int(b))
            elif tok == '*':
                a = stack.pop()
                b = stack.pop()
                print(a,b,tok)
                stack.append(int(a)*int(b))
            elif tok == '-':
                a = stack.pop()
                b = stack.pop()
                print(a,b,tok)
                stack.append(int(b)-int(a))
            elif tok == '/':
                a = stack.pop()
                b = stack.pop()
                print(a,b,tok)
           
                stack.append(int(int(b)/int(a)))
            else:
                stack.append(int(tok))
            
        return stack.pop()