class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}
    
        if len(s)%2 != 0 :
            return False
    
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if stack == []:
                    return False
                else:
                    if pairs[c] != stack[-1]:
                        return False
                    else:
                        stack.pop()
        if stack == []:
            return True
        else:
            return False
                