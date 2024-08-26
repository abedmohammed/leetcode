class Solution(object):
    def evalRPN(self, tokens):
        memory = []

        for token in tokens:
            if token not in "+-*/":
                memory.append(int(token))
            else:
                num2 = memory.pop()
                num1 = memory.pop()
                if token == "+":
                    memory.append(num1 + num2)
                elif token == "-":
                    memory.append(num1 - num2) 
                elif token == "*":
                    memory.append(num1 * num2) 
                elif token == "/":
                    memory.append(int(float(num1) / num2)) 

        return memory[-1]
    
answer = Solution()
print(answer.evalRPN(["2","1","+","3","*"]))
print(answer.evalRPN(["4","13","5","/","+"]))
print(answer.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))