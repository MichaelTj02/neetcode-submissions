class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) <= 1:
            return int(tokens[0])
        stack = []
        operators = ["+", "*", "-", "/"]

        for elem in tokens:
            if elem not in operators:
                stack.append(elem)
            else:
                res = 0
                if elem == '+':
                    res = int(stack[-1]) + int(stack[-2])
                elif elem == '-':
                    res = int(stack[-2]) - int(stack[-1])
                elif elem == '*':
                    res = int(stack[-1]) * int(stack[-2])
                elif elem == '/':
                    res = int(stack[-2]) / int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(int(res))
                print(stack)
        return stack[-1]