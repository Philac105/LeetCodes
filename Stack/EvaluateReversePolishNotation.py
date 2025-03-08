from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        number_stack = []

        while len(tokens) > 0:
            token = tokens.pop(0)
            if token == "+":
                b, a = number_stack.pop(), number_stack.pop()
                number_stack.append(a + b)
            elif token == "-":
                b, a = number_stack.pop(), number_stack.pop()
                number_stack.append(a - b)
            elif token == "*":
                b, a = number_stack.pop(), number_stack.pop()
                number_stack.append(a * b)
            elif token == "/":
                b, a = number_stack.pop(), number_stack.pop()
                number_stack.append(int(a / b))
            else:
                number_stack.append(int(token))

        return number_stack.pop()
