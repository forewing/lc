class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x // y if x * y >= 0 else -(-x // y),
        }
        for token in tokens:
            if token in op:
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(op[token](n1, n2))
            else:
                stack.append(int(token))
        return stack.pop()
