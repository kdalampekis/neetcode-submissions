class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for c in tokens:
            if c == "+" or c == "-" or c == "*" or c =="/" and operands!=[]:
                if c == "+":
                    results  = int(operands[-1]) + int(operands[-2])
                    operands.pop()
                    operands.pop()
                    operands.append(int(results))
                elif c == "-":
                    results  = int(operands[-2]) - int(operands[-1])
                    operands.pop()
                    operands.pop()
                    operands.append(int(results))
                elif c == "*":
                    results  = int(operands[-1]) * int(operands[-2])
                    operands.pop()
                    operands.pop()
                    operands.append(int(results))
                elif c == "/":
                    results  = int(operands[-2]) / int(operands[-1])
                    operands.pop()
                    operands.pop()
                    operands.append(int(results))
            else:
                operands.append(int(c))
        return operands[-1]
