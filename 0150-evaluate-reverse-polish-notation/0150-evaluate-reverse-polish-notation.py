import math

class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for i in tokens:
            if i not in ['+', '-', '*', '/']:
                stack.append(int(i))
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if i == '+':
                    stack.append(num1 + num2)
                elif i == '-':
                    stack.append(num1 - num2)
                elif i == '*':
                    stack.append(num1 * num2)
                else:  # division, truncate toward zero
                    stack.append(math.trunc(num1 / num2))

        return stack.pop()
