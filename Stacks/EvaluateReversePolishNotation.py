class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if tokens is None or len(tokens) < 1: return 0
        stack = []

        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
            else:
                var1 = stack.pop()
                var2 = stack.pop()
                if token == '+':
                    stack.append(var1 + var2)
                elif token == '-':
                    stack.append(var2 - var1)
                elif token == '*':
                    stack.append(var1 * var2)
                elif token == '/':
                    stack.append(0) if var1 == 0 else stack.append(int(var2 / var1))

        if len(stack) != 0: return stack.pop()


s = Solution()
print(s.evalRPN(["2", "1", "+", "3", "*"]))